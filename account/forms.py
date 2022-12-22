from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    
    email = forms.CharField()
    username = forms.CharField(label = 'Usuario',max_length=20)
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label='Apellido')
    descripcion = forms.CharField(label='Descripcion')
    link_pag = forms.CharField(label='Link a mi página')
    avatar = forms.ImageField(required=False)