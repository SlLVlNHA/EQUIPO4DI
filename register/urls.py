from django.contrib import admin
from django.urls import include, path

# Views
from . import views

urlpatterns = [
	path("", views.RegisterView.as_view(), name="register"),
]