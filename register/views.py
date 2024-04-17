# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import TemplateView
from home.models import Client
from .forms import SignUpForm 
from django.contrib.auth import login,authenticate

# Create your views here.
class RegisterView(CreateView):
    template_name = "register/register.html"
    model = Client 
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En esta parte, si el form es valido lo guardamos y usamos authenticate e iniciamos sesión
        '''
        print("Pasamos wiiiiiii")
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario,password=password)
        print("Pasamos wiiiiiii")
        login(self.request, usuario)
        print("Pasamos wiiiiiii")
        return redirect('/tablero') #aqui?