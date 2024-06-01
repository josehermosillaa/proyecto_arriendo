from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('rut','direccion','telefono','correo')
    
