from django.db import models
from django.contrib.auth.models import User

from home.models import Client
# Create your models here.
COLOR_STATUS = (
    (0, '#F98866'),
    (1, '#FF420E'),
    (2, '#80BD9E'),
    (3, '#89DA59'),
)

class Card(models.Model):
    """Tarjetas"""
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=300)
    color=models.IntegerField(choices=COLOR_STATUS)
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 