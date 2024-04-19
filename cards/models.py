from django.db import models
from django.contrib.auth.models import User

from home.models import Client
# Create your models here.
COLOR_STATUS = (
    (0,'PaleTurquoise'), #B9DDDA
    (1,'CadetBlue'), #58ACA4
    (2,'Pink'), #FBBDBE
    (3,'Puce'), #D68A95
)

class Card(models.Model):
    """Tarjetas"""
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    color=models.IntegerField(choices=COLOR_STATUS)
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 