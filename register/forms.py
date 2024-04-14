from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=140, required=True)     
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    def clean_username(self):
        print("¡Dónde está el pedo1?")  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El usuario ya existe")  
        return username

    def save(self, commit = True):
        print("¡Dónde está el pedo2?")  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  #¿Asi?
        )  
        return user

    def clean_password(self):
        print("¡Dónde está el pedo3?")  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas estan muy mal")  
        return password1

    def clean_email(self):  
        print("¡Dónde está el pedo4?")
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El e-mail introdiucido ya existe")  
        return email

