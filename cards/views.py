from django.shortcuts import render
from .models import Card
from django.db.models import Q
from django.views import View
from .forms import CardForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

#Creacion de una nueva nota
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    success_url = '/tablero/'  

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

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
    success_url = '/tablero/'  # URL a la que se redirigirá después de eliminar correctamente la nota
    template_name = 'cards/delete_card.html'  # Plantilla que se utilizará para mostrar la confirmación de eliminación

class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    success_url = '/tablero/'
#Mau
class BlogSearchView(ListView):
    model = Card
    template_name = 'card_list.html'
    context_object_name = 'cards'
    paginate_by = 6
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

        return queryset
