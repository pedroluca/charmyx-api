from django.db import models
from pessoa.models import Pessoa

class Proprietario(Pessoa):
    especializacao = models.CharField(max_length=50)