from django.db import models
from admin_rh.models import Employe
# importer validtors: Ces validateurs sont passés en paramètre dans l'attribut validators du champ note_evaluation . Cela garantit que la note sera toujours validée entre 0 et 5
from django.core.validators import MinValueValidator, MaxValueValidator

# importer ValidationError pour fonction clean 
# from django.core.exceptions import ValidationError

# Création du modèle pour les évaluations
class Évaluation(models.Model):
    manager = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='evaluations_as_manager',null=True, blank=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='evaluations_as_employe',null=True, blank=True)
    date_évaluation = models.DateField()
    note_evaluation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    commentaire = models.CharField(max_length=1500)
   

    def __str__(self):
        return f"Évaluation pour l'employé : {self.employe.nom}"  


