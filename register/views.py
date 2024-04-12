# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.views.generic import TemplateView
# Create your views here.
class RegisterView(TemplateView):
    """New User Sign Up."""
    template_name = "register/register.html"