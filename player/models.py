from django.db import models

# Create your models here.

class Player(models.Model):
    nume = models.CharField(max_length=255)
    prenume = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nume_utilizator = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    experienta = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)

class Skills(models.Model):
    nume = models.CharField(max_length=255)
    descriere = models.CharField(max_length=255)
    tip = models.CharField(max_length=255)
    puncte = models.IntegerField(default=0)
    level_necesar = models.IntegerField(default=0)
    caracteristica_necesara = models.CharField(max_length=255)
    caracteristica_puncte_necesare = models.IntegerField(default=0)
    player = models.ManyToManyField(Player)