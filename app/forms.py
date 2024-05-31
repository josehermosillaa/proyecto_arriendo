from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class PerfilForm(forms.Form):
    TIPO =((1,'Arrendador'),(2,'Arrendatario'))
    """el correo y el usuario son datos que podemos obtener desde auth.USER
    se almacenan al iniciar sesion en el sistema
    usuario
    correo
    """
    tipo = forms.ChoiceField(choices=[TIPO], required=True)
    rut = forms.CharField(label='rut', max_length=100)
    direccion = forms.CharField(label='direcion', max_length=100)
    telefono = forms.CharField(label='direcion', max_length=100)
    
