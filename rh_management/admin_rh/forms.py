from django.db.models import fields
from django import forms
from .models import Employe,Service,Absence,Massrouf,Recrutement
from django.contrib.auth.forms import UserCreationForm
  
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



class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")