
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from player.models import Player, Skills
from django.core import serializers
import json, random

def check(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponse("404 record not found.")
    return inner

class Engine:

    def convert_model_to_json(self, model_record):
        if not model_record:
            return {}
        if type(model_record) is not list: 
            model_record = [model_record, ]
        model_string = serializers.serialize('json', model_record)
        if not model_string:
            return {}
        return json.loads(model_string)
   
    def fight(self, player_id: int, enemy_id: int):
        try:
            player = self.convert_model_to_json(Player.objects.get(id = player_id))
            enemy = self.convert_model_to_json(Player.objects.get(id = enemy_id))        
        except ObjectDoesNotExist:
            return {
                'player': {},
                'enemy': {}
            }
        return { 
            'player': self.setId(player), 
            'enemy': self.setId(enemy)
        }
    
    def setId(self, player):
        if type(player) is list and len(player):
            player[0]['fields']['id'] = player[0]['pk']
            return player[0]['fields']
        return player

    @check
    def hit(self, player, enemy):
        if random.randint(0,100) < player['luck']: # chance geting min attack or full is by the number of luck
            hitAttack = player['attack'] # full attack
        else:
            hitAttack = (50 * player['attack'] ) / 100 # min attack is 50% pf player full attack
        enemy['health'] = (enemy['health'] - hitAttack)
        return { 
            'player': player, 
            'enemy': enemy
        }