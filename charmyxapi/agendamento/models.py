from django.db import models
from cliente.models import Cliente

# Create your models here.

class Agendamento(models.Model):
    horario = models.TimeField()
    data = models.DateField()
    observacao = models.TextField()
    STATUS_CHOICES = [
        ('PEN', 'Pendente'),
        ('CON', 'Confirmado'),
        ('FIN', 'Concluído'),
    ]
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='PEN',
        verbose_name="Status do Serviço",
        help_text="Estado atual do serviço"
    )
    # servico_id = models.ForeignKey(Servico, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

  