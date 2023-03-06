from django.urls import path, include

from . import views


urlpatterns = [
   path("accounts/", include("django.contrib.auth.urls")),
   path("accounts/login", views.LoginView.as_view(), name = "login"),
   path("signup/", views.SignUpView.as_view(), name = 'signup'),
   path("logout", views.logout, name="logout"),
   path('', views.home, name="home"),
   path('home/', views.home, name="home"),
   path("ingredients/", views.IngredientsView.as_view(), name='ingredients'),
   path("ingredients/new/", views.IngredientCreate.as_view(), name='addingredient'),
   path("ingredients/<pk>/update", views.UpdateIngredientView.as_view(), name='update_ingredient'),
   path("ingredients/<pk>/delete", views.DeleteIngredientView.as_view(), name='delete_ingredient'),
   path("menu/", views.MenuItemView.as_view(), name='menu'),
   path("menu/new/", views.MenuItemCreate.as_view(), name='addmenuitem'),
   path("menu/<pk>/update", views.UpdateMenuItemView.as_view(), name='update_menu'),
   path("menu/<pk>/delete", views.DeleteMenuItemView.as_view(), name='delete_menu'),
   path("purchases/", views.PurchaseView.as_view(), name='purchase'),
   path("purchase/new/", views.PurchaseCreate.as_view(), name='addpurchase'),
   path("purchases/<pk>/delete", views.DeleteMenuItemView.as_view(), name='delete_purchase'),
   path('menu/<slug:menuitem>/', views.requirements, name='requirements'),
   path("requirement/new/", views.RecipeRequirementCreate.as_view(), name='addrequirement'),
   path("sales/", views.SalesView.as_view(), name='sales'),
   
   
   
]