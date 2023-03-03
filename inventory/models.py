from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal
# from money import Money
from moneyed import Money, KES
from moneyed.l10n import format_money
from .fields import CaseInsensitiveCharfield

# from model_utils import Choices

UNITS = (("kilogram", "kilogram"),
         ("litre", "litre"),
         (None, ""))

from django.core.validators import MinValueValidator

class Ingredient(models.Model):
    name = CaseInsensitiveCharfield(max_length=50, unique=True)
    unit = models.CharField(choices=UNITS, max_length=20, blank=True, null=True)
    price = models.DecimalField("price per unit", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.DecimalField(default=10.0, decimal_places=2, max_digits=12, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"{self.name}"
    def get_absolute_url(self):
        return "/ingredients/"
        


class MenuItem(models.Model):
    name = CaseInsensitiveCharfield(max_length=50, unique=True)
    price = models.DecimalField("price of item", max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self):
        return f"{self.name}"
    def get_absolute_url(self):
        return "/menu/"
class RecipeRequirement(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(0)])
    def __str__(self):
        return f"menu item: {self.item}, ingredient: {self.ingredient}"
    def available(self):
        s= Ingredient.objects.get(id=self.item.id)
        return s.quantity >= self.quantity
    def get_absolute_url(self):
        return "/requirements/"
    
    class Meta:
        constraints= [models.UniqueConstraint(fields=['item', 'ingredient'], name="no_duplicates")]
    
class Purchase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.quantity} {self.item}s bought at {self.timestamp}"
    
    def get_absolute_url(self):
        return "/purchases/"
    
    def cost(self):
        total = Money(0, KES)
        reqs = RecipeRequirement.objects.filter(item=self.item).all()
        for req in reqs:
            price = Decimal(req.quantity) * Decimal(req.ingredient.price)
            total += Money(price, currency='KES')
        return format_money(total, u'#,##0.00', locale='en_KE')
    
    def revenue(self):
        return format_money(Decimal(self.item.price )* self.quantity, u'#,##0.00', locale='en_KE')


    def save(self, *args, **kwargs):
        reqs = RecipeRequirement.objects.filter(item=self.item.id)
        for req in reqs:
            if req.available():
                ingredient = req.ingredient
                ingredient.quantity -= self.quantity * req.quantity
                ingredient.save()
        super(Purchase, self).save(*args, **kwargs)

    
   

