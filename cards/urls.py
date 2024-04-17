from django.urls import path
from . import views

urlpatterns = [
    path('',views.CardListView.as_view(),name='tablero'),
    path('delete/<int:pk>', views.CardDeleteView.as_view(), name='delete_card'), #Abraham
    path('search-blogs/',views.BlogSearchView.as_view(), name='search_blogs'), #Mau
    path('new/', views.CardCreateView.as_view(), name='new_card'), #Gabriela
    path('edit/<int:pk>', views.CardUpdateView.as_view(), name='update_card'), #AlexP

]
