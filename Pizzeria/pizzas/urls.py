from django.urls import path
from . import views

urlpatterns = [
    path('pizzas/', views.pizzas, name='pizzas'),
]