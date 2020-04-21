from django.shortcuts import render, redirect
from player.forms import RegisterPlayerForm, LoginPlayerForm
from player.models import Player, Skills

def index(request):
    return render(request, 'player/index.html')

def create(request):
    if request.method == 'POST':
        create_form_player = RegisterPlayerForm(request.POST)
        login_form_player = LoginPlayerForm(request.POST)
        if login_form_player.is_valid():
            return redirect('show_profile')
    else:
        create_form_player = RegisterPlayerForm(request.GET or None)
        login_form_player = LoginPlayerForm(request.GET or None)

    return render(request, 'player/create.html',{
        'create_form_player': create_form_player,
        'login_form_player': login_form_player,
        'method': 'creare'
    })
