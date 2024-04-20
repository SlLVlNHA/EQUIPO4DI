"""Home URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from . import views

urlpatterns = [
	path("", views.HomeView.as_view(), name="login"),
    path('logout_view/', views.logout_view, name='logout_view'), #Todos
]