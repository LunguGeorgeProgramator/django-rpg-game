from django.shortcuts import render
from player.models import Player, Skills
from django.http import JsonResponse
from engine.core_class import Engine
from django.http import HttpResponse
import json

def engine(request, id, id_e):
    data_to_return = Engine().fight(id, id_e)
    return JsonResponse(data_to_return, safe=False)

def hit(request, id, id_e):
    if request.method == 'POST':
        form_data = json.loads(request.body.decode())
    data_to_return = Engine().hit(form_data['player'], form_data['enemy'])
    return JsonResponse(data_to_return, safe=False)