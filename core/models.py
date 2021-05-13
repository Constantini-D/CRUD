from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    aniversario = models.DateField()

    def __str__(self):
        return self.nome