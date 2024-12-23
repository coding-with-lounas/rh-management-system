from django.db import models

# Create your models here.

class Employee(models.Model):
    Nom=models.CharField(max_length=50)
    Date_Naissance=models.DateField()
    Date_Embauche =models.DateField()
    Adresse=models.CharField
    service=models.ForeignKey('Service',on_delete=models.CASCADE)

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
     Date_Évaluation=models.DateField()
     Score=models.FloatField()
     Objectifs_Attendus=models.FloatField()
     Objectifs_Atteints=models.FloatField()
    

class Salaire(models.Model):
     Mois
    Année
    Montant_Paye
    Retenues
    Primes
 

class Recrutement(models.Model):
 concerne
 Poste
 Date_Publication
 Statut


class Candidat(models.Model):
    Nom=models.CharField(max_length=50)
    Prénom=models.CharField(max_length=50)
    Email=models.EmailField()
    cv= models.FileField(upload_to='resumes/', null=True, blank=True)