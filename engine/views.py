from django.shortcuts import render
from player.models import Player, Skills
from django.http import JsonResponse
# from player.engine import Engine

def engine(request, id):
    data_to_return = []
    return JsonResponse(list(data_to_return), safe=False)