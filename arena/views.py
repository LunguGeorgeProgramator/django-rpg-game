from django.shortcuts import render
from player.models import Player, Skills
import random


def index(request):
    players = Player.objects
    if players:
        enemy = random.choice(players.all())
    if enemy and players.count() > 1:
        print(random.choice(players.all()))
    return render(request, 'arena/index.html')