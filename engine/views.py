from django.shortcuts import render
from player.models import Player, Skills
from django.http import JsonResponse
from engine.core_class import Engine
import json

def engine(request, id, id_e):
    data_to_return = Engine().fight(id, id_e)
    return JsonResponse(data_to_return, safe=False)