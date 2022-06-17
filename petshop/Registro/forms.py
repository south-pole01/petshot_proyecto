from django import forms
from .models import Departamento, Producto

class DeptoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'tipo', 'stock']

        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo departamento',
            'stock': 'Stock departamento',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

