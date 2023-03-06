from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientCreateForm, MenuItemCreateForm, PurchaseCreateForm, RecipeRequirementCreateForm


class LoginView(LoginView):
  template_name = "registration/login.html"
  success_url = reverse_lazy("home")
class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout(request):
  logout(request)
  return redirect("login")

@login_required
def home(request): 
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/home.html', {'ingredients': ingredients})

class IngredientsView(LoginRequiredMixin,ListView):
  model = Ingredient
  template_name = 'inventory/ingredients.html'

class IngredientCreate(LoginRequiredMixin,CreateView):
  model=Ingredient
  template_name = 'inventory/ingredient_create_form.html'
  form_class = IngredientCreateForm

class UpdateIngredientView(LoginRequiredMixin,UpdateView):
  model = Ingredient
  form_class = IngredientCreateForm
  template_name = "inventory/update_ingredient.html"

class DeleteIngredientView(LoginRequiredMixin,DeleteView):
  model = Ingredient
  template_name="inventory/delete_ingredient.html"
  success_url = "/ingredients"

class MenuItemView(LoginRequiredMixin,ListView):
  model = MenuItem
  template_name = 'inventory/menu_item.html'

class MenuItemCreate(LoginRequiredMixin,CreateView):
   model = MenuItem
   template_name='inventory/menu_item_create_form.html'
   form_class = MenuItemCreateForm

class UpdateMenuItemView(LoginRequiredMixin,UpdateView):
  model = MenuItem
  form_class = MenuItemCreateForm
  template_name = "inventory/update_menu.html"

class DeleteMenuItemView(LoginRequiredMixin,DeleteView):
  model = MenuItem
  template_name="inventory/delete_menu.html"
  success_url = "/menu"

class PurchaseView(LoginRequiredMixin,ListView):
  model = Purchase
  template_name = 'inventory/purchase.html'

class PurchaseCreate(LoginRequiredMixin,CreateView):
   model = Purchase
   template_name='inventory/purchase_form.html'
   form_class = PurchaseCreateForm

class DeletePurchaseView(LoginRequiredMixin,DeleteView):
  model = Purchase
  template_name="inventory/delete_purchase.html"
  success_url = "/purchases"

class RecipeRequirementCreate(LoginRequiredMixin,CreateView):
   model = RecipeRequirement
   template_name='inventory/recipe_requirement_create_form.html'
   form_class = RecipeRequirementCreateForm

class UpdateIngredientView(LoginRequiredMixin,UpdateView):
  model = Ingredient
  form_class = IngredientCreateForm
  template_name = "inventory/update_ingredient.html"
@login_required
class RequirementsDetail(LoginRequiredMixin, DetailView):
  model = MenuItem
  template_name = "inventory/reqirements.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = self.object
    recipe_requirements = RecipeRequirement.objects.filter(menu_item = self.object)
    ingredients = []
    for item in recipe_requirements:
      ingredients.append(item.ingredient)
    context['ingredients'] = ingredients
    return context

class SalesView(LoginRequiredMixin,ListView):
  model = Purchase
  template_name = 'inventory/sales.html'