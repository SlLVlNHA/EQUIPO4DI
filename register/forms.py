from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder": "Nombre de usuario"
    })) 
    email = forms.EmailField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input",
        "type":"email",
        "placeholder": "Dirección de email"
    }))     
    password1 = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder": "Contraseña",
    })) 
    password2 = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder": "Confirma tu contraseña"
    })) 
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )       

    def clean_username(self):        
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El usuario ya existe")  
        return username

    def save(self, commit = True):        
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user

    def clean_password(self):       
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")  
        return password1

    def clean_email(self):          
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El e-mail introducido ya existe")  
        return email

