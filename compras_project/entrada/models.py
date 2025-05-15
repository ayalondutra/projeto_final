from django.db import models

class Entrada(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto} - {self.quantidade} unidades"
