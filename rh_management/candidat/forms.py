# forms.py
from django import forms
from .models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ['nom', 'prénom', 'email', 'cv', 'recrutement']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prénom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'recrutement': forms.Select(attrs={'class': 'form-control'}),
        }
