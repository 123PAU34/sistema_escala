from django.db import models

class AvaliacaoNeurologica(models.Model):
    paciente = models.CharField(max_length=200)
    resultado = models.TextField()

    def __str__(self):
        return self.paciente

# Create your models here.
