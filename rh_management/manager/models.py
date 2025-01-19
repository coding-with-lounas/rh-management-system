from django.db import models

# importer validtors: Ces validateurs sont passés en paramètre dans l'attribut validators du champ note_evaluation . Cela garantit que la note sera toujours validée entre 0 et 5
from django.core.validators import MinValueValidator, MaxValueValidator

# importer ValidationError pour fonction clean 
# from django.core.exceptions import ValidationError

# Création du modèle pour les évaluations
class Évaluation(models.Model):
    date_évaluation = models.DateField()  
    note_evaluation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])  
    commentaire = models.CharField(max_length=1500)
    
    # def clean(self):
        
    #     if not (0 <= self.note_evaluation <= 5):
    #         raise ValidationError({'note_evaluation': 'La note doit être entre 0 et 5.'})  

    def __str__(self):
        return f"Évaluation pour l'employé :"

