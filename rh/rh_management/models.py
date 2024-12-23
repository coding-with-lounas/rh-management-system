from django.db import models

# Create your models here.

class Employee(models.Model):
    Nom=models.CharField(max_length=50)
    Date_Naissance=models.DateField()
    Date_Embauche =models.DateField()
    Adresse=models.CharField
    service=models.ForeignKey(Service,on_delete=models.CASCADE)

class Service(models.Model):
 Description=models.CharField(max_length=50)
 Nom_Service =models.CharField(max_length=50)

class Contrat(models.Model):
 Type_Contrat=models.CharField(max_length=50)
 Date_Début=models.DateField()
 Date_Fin=models.DateField()
 Salaire_Base=models.FloatField()

class Congé(models.Model):
 Type_Congé=models.CharField(30)
 Date_Début=models.DateField()
 Date_Fin=models.DateField()
 Solde_Congé=models.FloatField()

class Évaluation(models.Model):
 Salaire=models.DateField()
 Date_Évaluation=models.
 Score
 Objectifs_Attendus
 Objectifs_Atteints
 ID_Employé *