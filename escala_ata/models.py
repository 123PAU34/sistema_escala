from django.db import models
class ATA(models.Model):
    nome = models.CharField(max_length=200)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome
# Create your models here.
