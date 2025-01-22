from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # employe
    path('employe/',views.afficherEmploye,name='empList'),
    path('employe/ajouterEmploye/',views.ajouterEmploye,name='addemp'),
    path('employe/supprimerEmploye/<int:pk>/', views.supprimerEmploye, name='delemp'),
    path('employe/modifierEmploye/<int:pk>/', views.modifierEmploye, name='editemp'),
    path('employe/rechercher',views.rechercherEmploye,name='rechercheList'),
    # Service
    # path('services/',views.afficherService, name='afficherService'),
    path('services/',views.nbr_emp_par_service,name='serviceList'),
    path('service/ajouter/', views.ajouterService, name='ajouterService'), 
    path('service/modifier/<int:pk>/', views.modifierService, name='modifierService'),  
    path('service/supprimer/<int:pk>/', views.supprimerService, name='supprimerService'),
    path('services/recherche/', views.rechercherService, name='rechercherService'),  
    # absence
    path('ajouter-absence/', views.ajouterAbsence, name='ajouterAbsence'),
    path('editer-absence/<int:pk>/', views.editerAbsence, name='editerAbsence'),
    path('supprimer-absence/<int:pk>/', views.supprimerAbsence, name='supprimerAbsence'),
    path('absences/', views.afficherAbsences, name='listeAbsences'),
    path('absences/rechercher/', views.rechercherAbsences, name='rechercher_absences'),
    #    Massrouf 
    path('demande_massrouf/<int:employe_id>/', views.demande_massrouf, name='demande_massrouf'),
    # contrat 
    path('contrats/', views.afficherContrat, name='contratList'),
    path('contrats/add/', views.ajouterContrat, name='addContrat'),
    path('contrats/edit/<int:pk>/', views.modifierContrat, name='editContrat'),
    path('contrats/delete/<int:pk>/', views.supprimerContrat, name='deleteContrat'),
    path('contrats/search/', views.rechercherContrat, name='searchContrat'),
    # recrutemnnt
    path('recrutements/', views.afficherRecrutements, name='listeRecrutements'), 
    path('recrutement/ajouter/', views.ajouterRecrutement, name='ajouterRecrutement'), 
    path('recrutement/editer/<int:pk>/', views.editerRecrutement, name='editerRecrutement'),  
    path('recrutement/supprimer/<int:pk>/', views.supprimerRecrutement, name='supprimerRecrutement'),  
    # analyse
    path('analyse-absences/', views.analyse_absences, name='analyse_absences'),
    path('analyse-activite/', views.analyseActivite, name='analyseActivite'),
    # Authentification
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]
