from django.shortcuts import render
from player.models import Player, Skills
from engine.core_class import check
import random

def getEnemy(id, count = 0):
    players = Player.objects
    if players:
        enemy = random.choice(players.all())
        while (enemy.id == id):
            enemy = random.choice(players.all())
            if count > 4:
                break 
            count += 1   
    if enemy and players.count() > 1:
        return enemy   
    return None

@check
def index(request, id):
    enemy = getEnemy(id)
    player = Player.objects.get(id=id)
    return render(request, 'arena/index.html', {'enemy': enemy, 'player': player})