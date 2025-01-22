from django import forms
from .models import Évaluation
from admin_rh.models import Employe

class ÉvaluationForm(forms.ModelForm):
    class Meta:
        model = Évaluation
        fields = ['manager', 'employe', 'date_évaluation', 'note_evaluation', 'commentaire']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
