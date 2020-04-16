from django.db import models

# Create your models here.

class Player(models.Model):
    nume = models.CharField(max_length=255)
    prenume = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nume_utilizator = models.CharField(max_length=255)