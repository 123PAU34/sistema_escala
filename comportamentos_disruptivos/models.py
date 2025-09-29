from django.db import models
from django.db import models

class Comportamento(models.Model):
    nome = models.CharField(max_length=200)
    frequencia = models.IntegerField()

    def __str__(self):
        return self.nome

# Create your models here.
