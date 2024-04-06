from django.shortcuts import render
from .models import Card

from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.
class CardListView(ListView):
    model = Card
    context_object_name = 'cards'

class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'
