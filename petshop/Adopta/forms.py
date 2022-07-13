from .models import Adopta
from django import forms

class AdoptaForm(forms.ModelForm):
    

    class Meta:
        model = Adopta
        fields = (
            'fotografia',
            'nombreMascota',
            'edad',
            'ciudad',
            'email',
            'tipo_animal',
        )
        labels = {
            'fotografia':'Fotografía',
            'nombreMascota':'Nombre Mascota',
            'edad':'Edad Mascota',
            'ciudad':'Ciudad de origen',
            'email':'Correo electrónico',
            'tipo_animal':'Tipo de animal',
        }
        widgets = {
            # 'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'nombreMascota':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form_control'}),
            'tipo_animal':forms.Select(choices="ANIMALES", attrs={'class':'form-control'}),
        }

