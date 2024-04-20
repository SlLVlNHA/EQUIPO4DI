from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import LoginForm 
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout

# Create your views here.
class HomeView(LoginView):
    """New User Sign Up."""

    template_name = "home/login.html"
    form_class = LoginForm    

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/tablero') 
        else:            
            return render(self.request, self.template_name, {'form': form, 'error_message': 'Credenciales inválidas'})

def logout_view(request):
    logout(request)

    return redirect('/login')  