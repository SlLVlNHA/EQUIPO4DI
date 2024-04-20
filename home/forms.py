from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder": "Nombre de usuario"
    })) 
    password = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder": "Contraseña"
    }))  
