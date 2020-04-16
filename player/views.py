from django.shortcuts import render
from .models import Player

def index(request):
    return render(request, 'player/index.html')

def create(request):
    return render(request, 'player/create.html')
