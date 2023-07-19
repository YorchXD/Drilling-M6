from django import forms
from .models import VehiculoModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = VehiculoModel
        fields = "__all__"
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'})
        }
        
class RegistroUsuarioForm(UserCreationForm):
    email = User
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user