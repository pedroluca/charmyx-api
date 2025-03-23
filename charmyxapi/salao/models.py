from django.db import models
# from proprietario.models import Proprietario

# Create your models here.
class Salao(models.Model):
  # Define your fields here
  nome = models.CharField(max_length=100)
  endereco = models.CharField(max_length=200)
  descricao = models.TextField()
  CNPJ = models.CharField(max_length=14)
  telefone = models.CharField(max_length=15)
  # proprietario = models.ForeignKey('proprietario.Proprietario', on_delete=models.CASCADE)
  url_image = models.ImageField(upload_to='media/', blank=True, null=True, default='media/default-salon.jpeg')
  # Add more fields as needed

  def __str__(self):
    return self.nome  # Return a string representation of your model instance