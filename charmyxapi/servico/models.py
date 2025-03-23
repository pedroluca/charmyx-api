from django.db import models
from salao.models import Salao

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.DurationField()
    salao = models.ForeignKey(Salao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome