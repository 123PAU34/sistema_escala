from django.db import models

class LaudoPsicologico(models.Model):
    paciente = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.paciente

# Create your models here.
