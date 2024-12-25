from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('employe/',views.afficherEmploye,name='empList'),
    path('ajouterEmploye/',views.ajouterEmploye,name='addemp')
]