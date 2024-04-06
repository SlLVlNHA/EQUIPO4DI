from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    """Extended user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type=models.IntegerField(default=2)