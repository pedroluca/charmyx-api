from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pessoa (User):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)

    class Meta:
        abstract = True 