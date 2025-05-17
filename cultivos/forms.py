# forms.py
from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['tipo', 'fecha_siembra', 'fecha_cosecha', 'cantidad', 'descripcion']
        widgets = {
            'fecha_siembra': forms.DateInput(attrs={'type': 'date'}),
            'fecha_cosecha': forms.DateInput(attrs={'type': 'date'}),
        }
