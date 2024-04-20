from django.shortcuts import render
from .models import Card
from django.db.models import Q
from django.views import View
from .forms import CardForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .filters import CardFilter


#Creacion de una nueva nota
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    success_url = '/tablero/'  
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class CardListView(LoginRequiredMixin, ListView):
    template_name = 'card_list.html'
    context_object_name = 'cards'
    paginate_by = 6
    login_url = "/login/"

    def get_queryset(self):
        queryset = Card.objects.all()

        title_content = self.request.GET.get('title_content')
        color = self.request.GET.get('color')
        date = self.request.GET.get('date')

        if title_content:
            queryset = queryset.filter(title__icontains=title_content) | queryset.filter(content__icontains=title_content)

        if color:
            queryset = queryset.filter(color=color)

        if date:
            queryset = queryset.filter(date=date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_set = CardFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = filter_set.form

        return context

class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'

class CardDeleteView(LoginRequiredMixin,DeleteView):
    model = Card
    success_url = '/tablero/'  # URL a la que se redirigirá después de eliminar correctamente la nota
    template_name = 'cards/delete_card.html'  # Plantilla que se utilizará para mostrar la confirmación de eliminación
    login_url = "/login/"

class CardUpdateView(LoginRequiredMixin,UpdateView):
    model = Card
    form_class = CardForm
    success_url = '/tablero/' 
    login_url = "/login/"


#Mau
class BlogSearchView(ListView):
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
