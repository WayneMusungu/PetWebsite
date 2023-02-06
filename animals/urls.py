from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registerUser/',views.RegisterUser, name='registerUser'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
     path('add_pet/', views.add_pet, name='add_pet'),
]