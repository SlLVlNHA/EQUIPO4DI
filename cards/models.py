from django.db import models
from django.contrib.auth.models import User

from home.models import Client
# Create your models here.
COLOR_STATUS = (
    (0,'petal'), #F98866
    (1,'poppy'), #FF420E
    (2,'stem'), #80BD9E
    (3,'green'), #89DA59
    (4,'azul'),
    (5,'rojo'),
)

class Card(models.Model):
    """Tarjetas"""
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    color=models.IntegerField(choices=COLOR_STATUS)
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 