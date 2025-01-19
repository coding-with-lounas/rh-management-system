from django.db.models import fields
from django import forms
from .models import Employe,Service,Absence,Massrouf,Recrutement

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields="__all__"
        labels = {
            'date_embauche': 'Date d\'embauche ',
            'date_naissance': 'Date naissance',
            'email': 'Email',  
        }

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


class MassroufForm(forms.ModelForm):
    class Meta:
        model = Massrouf
        fields = ['prix_avance', 'justification']
      

class RecrutementForm(forms.ModelForm):
    class Meta:
        model = Recrutement
        fields = ['poste', 'date_publication', 'statut']