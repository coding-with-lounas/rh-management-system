from django.db.models import fields
from django import forms
from .models import Employee

class EmpoloyeForm(forms.ModelForm):
class Meta:
model = Employee
fields="__all__"