
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from player.models import Player, Skills
from django.core import serializers
import json

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
            'player': player[0]['fields'] if type(player) is list and len(player) > 0 else {}, 
            'enemy': enemy[0]['fields'] if type(enemy) is list and len(enemy) > 0 else {}
        }
    
    def hit(self, attack, health):
        print(attack, health)
        return {1: 'da'}