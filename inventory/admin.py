from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)