from django.db.models import fields
from django import forms
from .models import Employe,Service,Absence

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields="__all__"
        labels = {
            'date_embauche': 'Date d\'embauche ',
            'date_naissance': 'Date naissance',
            'email': 'Email',  
        }
        # error_messages = {
        #     'nom': {
        #         'required': 'Le nom est obligatoire, veuillez le remplir.'
        #     },
        #     'prenom': {
        #         'required': 'Le prénom est obligatoire, veuillez le remplir.'
        #     },
        #     'adresse': {
        #         'required': 'L\'adresse est obligatoire, veuillez la remplir.'
        #     },
        #     'email': {
        #         'required': 'L\'email est nécessaire pour l\'inscription.'
        #     },
        #     'date_naissance': {
        #         'required': 'La date de naissance est obligatoire.'
        #     },
        #     'date_embauche': {
        #         'required': 'La date d\'embauche est obligatoire.'
        #     },
        #     'service': {
        #         'required': 'Le service est nécessaire pour cet employé.'
        #     },
        # }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom_service', 'description']
        


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['employe', 'date_Absence', 'justification']
        labels = {
            'employe': 'Employé',
            'date_Absence': 'Date d\'absence',
            'justification': 'Justification',
        }