from django.db import models
from pessoa.models import Pessoa

class Cliente(Pessoa):
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.username
    