from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientCreateForm, MenuItemCreateForm, PurchaseCreateForm, RecipeRequirementCreateForm

def home(request): 
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/home.html', {'ingredients': ingredients})

class IngredientsView(ListView):
  model = Ingredient
  template_name = 'inventory/ingredients.html'

class IngredientCreate(CreateView):
  model=Ingredient
  template_name = 'inventory/ingredient_create_form.html'
  form_class = IngredientCreateForm

class UpdateIngredientView(UpdateView):
  model = Ingredient
  form_class = IngredientCreateForm
  template_name = "inventory/update_ingredient.html"

class DeleteIngredientView(DeleteView):
  model = Ingredient
  template_name="inventory/delete_ingredient.html"
  success_url = "/ingredients"

class MenuItemView(ListView):
  model = MenuItem
  template_name = 'inventory/menu_item.html'

class MenuItemCreate(CreateView):
   model = MenuItem
   template_name='inventory/menu_item_create_form.html'
   form_class = MenuItemCreateForm

class UpdateMenuItemView(UpdateView):
  model = MenuItem
  form_class = MenuItemCreateForm
  template_name = "inventory/update_menu.html"

class DeleteMenuItemView(DeleteView):
  model = MenuItem
  template_name="inventory/delete_menu.html"
  success_url = "/menu"

class PurchaseView(ListView):
  model = Purchase
  template_name = 'inventory/purchase.html'

class PurchaseCreate(CreateView):
   model = Purchase
   template_name='inventory/purchase_form.html'
   form_class = PurchaseCreateForm

class DeletePurchaseView(DeleteView):
  model = Purchase
  template_name="inventory/delete_purchase.html"
  success_url = "/purchases"

class RecipeRequirementCreate(CreateView):
   model = RecipeRequirement
   template_name='inventory/recipe_requirement_create_form.html'
   form_class = RecipeRequirementCreateForm

class UpdateIngredientView(UpdateView):
  model = Ingredient
  form_class = IngredientCreateForm
  template_name = "inventory/update_ingredient.html"

def requirements(request, menuitem_name):
    menuitem = get_object_or_404(MenuItem, name=menuitem_name)
    requirements = RecipeRequirement.objects.filter(item=menuitem).all()
    return render(request, 'inventory/requirements.html', {'menuitem': menuitem, 'requirements': requirements})

class SalesView(ListView):
  model = Purchase
  template_name = 'inventory/sales.html'