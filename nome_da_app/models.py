from django.db import models

class ATA(models.Model):
    nome = models.CharField(max_length=200)
    pontuacao = models.IntegerField()

# Create your models here.
