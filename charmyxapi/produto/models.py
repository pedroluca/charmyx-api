from django.db import models

# Create your models here.
class Produto(models.Model):
  url_image = models.ImageField(upload_to='produto/', blank=True, null=True, default='produto/default-product.png')
  nome = models.CharField(max_length=100)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  descricao = models.TextField()
  quantidade_estoque = models.IntegerField()
  salao = models.ForeignKey('salao.Salao', on_delete=models.CASCADE)

  def __str__(self):
    return self.nome