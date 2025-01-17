from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class Service(models.Model):
    nom_service = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_service


class Employe(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=10,choices=[('M', 'HOMME'), ('F', 'FEMME')],default='M')
    adresse=models.CharField(max_length=250)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=100)
    date_embauche = models.DateField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE,related_name="rel_emp")
    # salaire = models.ForeignKey(Salaire, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.prenom} {self.nom}'
    


class Salaire(models.Model):
    Salaire_jr = models.ForeignKey("Contrat", on_delete=models.CASCADE)
    employe=models.ForeignKey("Employe", on_delete=models.CASCADE,related_name="sal_emp")
    salaireMois = models.FloatField() 
    moisdetravail = models.IntegerField()  
    mois = models.CharField(max_length=10)  
    annee = models.IntegerField(default=now().year)  

    def __str__(self):
        return f"Salaire : {self.salaireMois} DA - Mois : {self.mois} {self.annee}"

class Massrouf(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    prix_avance=models.DecimalField(max_digits=10, decimal_places=2)
    date_demande = models.DateField(auto_now_add=True)
    justification = models.TextField()
    
    def __str__(self):
        return f"Avance : {self.prix_avance} DA - {self.date_demande}"
    

class Pointage(models.Model):
    Employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    compteur = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
class Absence(models.Model):
    employe=models.ForeignKey(Employe, on_delete=models.CASCADE,related_name="rel_abs")
    date_Absence=models.DateField()
    justification=models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.employe.nom} - {self.date_Absence}"



class Contrat(models.Model):
    type_contrat = models.CharField(max_length=50)
    date_début = models.DateField()
    date_fin = models.DateField()
    salaireJrs = models.FloatField()  
    employe = models.OneToOneField("Employe", on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        if self.date_fin and self.date_début and self.date_fin <= self.date_début:
            raise ValidationError("La date de fin doit être postérieure à la date de début.")

    def __str__(self):
        return f"Contrat: {self.type_contrat}, Employé: {self.employe}, Durée: {self.date_début} - {self.date_fin}"




class Congé(models.Model):
    type_congé = models.CharField(max_length=30)
    date_début = models.DateField()
    date_fin = models.DateField()
    solde_congé = models.FloatField()

    def __str__(self):
        return f"{self.type_congé} ({self.date_début} - {self.date_fin})"


# class Évaluation(models.Model):
#     salaire = models.FloatField()
#     date_évaluation = models.DateField()
#     score = models.FloatField()
#     objectifs_attendus = models.FloatField()
#     objectifs_atteints = models.FloatField()

#     def __str__(self):
#         return f"Évaluation {self.date_évaluation}: Score {self.score}"


class Recrutement(models.Model):
    poste = models.CharField(max_length=50)
    date_publication = models.DateField()
    statut = models.CharField(max_length=50)

    def __str__(self):
        return f"Poste: {self.poste} ({self.statut})"


# class Candidat(models.Model):
#     nom = models.CharField(max_length=50)
#     prénom = models.CharField(max_length=50)
#     email = models.EmailField()
#     cv = models.FileField(upload_to='resumes/', null=True, blank=True)

#     def __str__(self):
#         return f"{self.nom} {self.prénom}"
