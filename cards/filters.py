import django_filters
from .models import Card

class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = {
            'title' : ['icontains'],
            'color' : ['exact'],
            'date' : ['exact']
        }