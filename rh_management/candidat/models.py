from django.db import models

# Create your models here.


class Candidat(models.Model):
    nom = models.CharField(max_length=50)
    prénom = models.CharField(max_length=50)
    email = models.EmailField()
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prénom}"