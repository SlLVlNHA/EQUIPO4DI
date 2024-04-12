from django.shortcuts import render
from .models import Card

from django.views import View
from django.views.generic import ListView, DetailView, DeleteView

# Create your views here.
class CardListView(ListView):
    model = Card
    paginate_by = 6
    context_object_name = 'cards'

class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'

class CardDeleteView(DeleteView):
    model = Card
    success_url = '/tablero/cards/''/cards/'  # URL a la que se redirigirá después de eliminar correctamente la nota
    template_name = 'cards/delete_card.html'  # Plantilla que se utilizará para mostrar la confirmación de eliminación
