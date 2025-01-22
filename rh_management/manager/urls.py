from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('evaluation', views.evaluation_create, name='evaluation_create'),
     path('evaluation/success/', views.evaluation_success, name='evaluation_success'),
]