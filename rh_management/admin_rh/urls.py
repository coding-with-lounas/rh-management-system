from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('employe/',views.afficherEmploye,name='empList'),
    path('employe/ajouterEmploye/',views.ajouterEmploye,name='addemp'),
    path('employe/supprimerEmploye/<int:pk>/', views.supprimerEmploye, name='delemp'),
    path('employe/modifierEmploye/<int:pk>/', views.modifierEmploye, name='editemp'),
]
