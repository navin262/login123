from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('wel/', views.wel),
]
