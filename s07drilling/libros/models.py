from django.db import models

# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField(help_text="Valor entre 0 a 10000")

    def __str__(self):
        return self.titulo