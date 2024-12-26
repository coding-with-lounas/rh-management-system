from django.db import models


class Service(models.Model):
    nom_service = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom_service


class Employe(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50) 
    adresse=models.CharField(max_length=250)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=100)
    date_embauche = models.DateField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE,related_name="rel_emp")

    def __str__(self):
        return f'{self.prenom} {self.nom}'


class Contrat(models.Model):
    type_contrat = models.CharField(max_length=50)
    date_début = models.DateField()
    date_fin = models.DateField()
    salaire_base = models.FloatField()

    def __str__(self):
        return f"{self.type_contrat} ({self.date_début} - {self.date_fin})"


class Congé(models.Model):
    type_congé = models.CharField(max_length=30)
    date_début = models.DateField()
    date_fin = models.DateField()
    solde_congé = models.FloatField()

    def __str__(self):
        return f"{self.type_congé} ({self.date_début} - {self.date_fin})"


class Évaluation(models.Model):
    salaire = models.FloatField()
    date_évaluation = models.DateField()
    score = models.FloatField()
    objectifs_attendus = models.FloatField()
    objectifs_atteints = models.FloatField()

    def __str__(self):
        return f"Évaluation {self.date_évaluation}: Score {self.score}"


class Salaire(models.Model):
    mois = models.CharField(max_length=20)
    année = models.IntegerField()
    montant_paye = models.FloatField()
    retenues = models.FloatField()
    primes = models.FloatField()

    def __str__(self):
        return f"Salaire: {self.mois} {self.année}"


class Recrutement(models.Model):
    poste = models.CharField(max_length=50)
    date_publication = models.DateField()
    statut = models.CharField(max_length=50)

    def __str__(self):
        return f"Poste: {self.poste} ({self.statut})"


class Candidat(models.Model):
    nom = models.CharField(max_length=50)
    prénom = models.CharField(max_length=50)
    email = models.EmailField()
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prénom}"
