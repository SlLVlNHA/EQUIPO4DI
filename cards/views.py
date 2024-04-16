from django.shortcuts import render
from .models import Card
from django.db.models import Q
from django.views import View
from .forms import CardForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView

#Creacion de una nueva nota
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    success_url = '/tablero/'  

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class CardListView(ListView):
    model = Card
    paginate_by = 6
    context_object_name = 'cards'

class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'

class CardDeleteView(DeleteView):
    model = Card
    success_url = '/tablero/'  # URL a la que se redirigirá después de eliminar correctamente la nota
    template_name = 'cards/delete_card.html'  # Plantilla que se utilizará para mostrar la confirmación de eliminación

#Mau
class CardSearchView(ListView):
    model = Card
    template_name = 'card_list.html'
    context_object_name = 'cards'
    paginate_by = 6
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        color = self.request.GET.get('color')

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

        if color:
            queryset = queryset.filter(color=color)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        color = self.request.GET.get('color')

        if not context['cards'] and (query or color):
            context['no_results_message'] = "No se encontraron tarjetas con esos criterios de búsqueda."

        return context
