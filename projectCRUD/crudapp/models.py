from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo= models.CharField(
        max_length=255,
        null= False,
        blank= False
    )

    autor = models.CharField(
        max_length= 255,
        null= False,
        blank=False
    )

    editora = models.CharField(
        max_length=255,
        null= False,
        blank=False
    )

    genero=models.CharField(
        max_length= 255,
        null= False,
        blank=False
    )

    preco = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=False,
        blank=False
    )

    tipo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

