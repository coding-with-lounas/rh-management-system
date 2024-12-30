from django import forms
from .models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ['nom', 'prénom', 'email', 'cv', 'recrutement']
 