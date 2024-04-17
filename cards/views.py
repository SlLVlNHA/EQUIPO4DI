from django.shortcuts import render
from .models import Card
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from .filters import CardFilter

# Create your views here.
class CardListView(ListView):
    #model = Card
    #paginate_by = 6
    #context_object_name = 'cards'
    queryset = Card.objects.all()
    template_name = 'card_list.html'
    context_object_name = 'cards'
    paginate_by = 6
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CardFilter(self.request.GET,queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'

class CardDeleteView(DeleteView):
    model = Card
    success_url = '/tablero/'  # URL a la que se redirigirá después de eliminar correctamente la nota
    template_name = 'cards/delete_card.html'  # Plantilla que se utilizará para mostrar la confirmación de eliminación

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
