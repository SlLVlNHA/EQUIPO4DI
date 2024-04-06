from django.urls import path
from . import views

urlpatterns = [
    path('cards/',views.CardListView.as_view(),name='tablero'),
    path('cards/<int:pk>',views.CardDetailView.as_view()),
]