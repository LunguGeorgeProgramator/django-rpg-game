from django.shortcuts import render, redirect
from player.forms import RegisterPlayerForm, LoginPlayerForm
from django.core.exceptions import ObjectDoesNotExist
from player.models import Player, Skills
from django.contrib.sessions.backends.db import SessionStore



def checkAuth(request, template = None, player_id = None):
    try:
        if request.session['player_id'] == player_id:
            return template
        else: 
            return redirect('login_profile')
    except KeyError:
        return redirect('login_profile')

def index(request):
    players = Player.objects.all()
    return render(request, 'player/index.html', { 'players': players })

def create(request):
    error = ''
    if request.method == 'POST':
        create_form_player = RegisterPlayerForm(request.POST)
        if create_form_player.is_valid():
            return store(request, create_form_player)
    else:
        create_form_player = RegisterPlayerForm(request.GET or None)
    return render(request, 'player/create.html',{
        'create_form_player': create_form_player,
        'error': error
    })

def store(request, create_form_player): 
    email = create_form_player.cleaned_data.get('email')
    player = Player.objects.filter(
        nume_utilizator = create_form_player.cleaned_data.get('nume_utilizator'), 
        email = email
    )
    if player:
        return render(request, 'player/create.html',{
            'create_form_player': create_form_player,
            'error': 'Email deja utilizat ' +  email
        })
    player = Player(
        nume = create_form_player.cleaned_data.get('nume'), 
        prenume = create_form_player.cleaned_data.get('prenume'), 
        nume_utilizator = create_form_player.cleaned_data.get('nume_utilizator'), 
        email = create_form_player.cleaned_data.get('email')
    )
    player.save()
    return redirect('show_profile', player.id)

def edit(request):
    return

def update(request):
    return

def logout(request):
    try:
        del request.session['player_id']
    except KeyError:
        pass
    return render(request, 'index.html')

def login(request):
    player = None
    error = ''
    if request.method == 'POST':
        login_form_player = LoginPlayerForm(request.POST)
        if login_form_player.is_valid():
            user_name = login_form_player.cleaned_data.get('nume_utilizator')
            player = Player.objects.filter(
                nume_utilizator = user_name, 
                email = login_form_player.cleaned_data.get('email')
            )
            if player:

                try:
                    request.session['player_id'] = player[0].id
                except KeyError:
                    s = SessionStore()
                    s['player_id'] = player[0].id
                    s.create()
                    s.session_key
                    s = SessionStore(session_key=s.session_key)

                return redirect('show_profile', id=player[0].id)
            else:
                error = 'Nu exista userul ' +  user_name
    else:
        login_form_player = LoginPlayerForm(request.GET or None)
    return render(request, 'player/login.html',{
        'login_form_player': login_form_player,
        'error': error 
    })

def show(request, id):
    try:
        player = Player.objects.get(id=id)
    except ObjectDoesNotExist:
        player = {
            'id': 0,
            'nume': 'XXX',
            'prenume': 'XXX',
            'email': 'XXX@XXX.XXX',
            'nume_utilizator': 'XXX',
            'level': 'XXX',
            'experienta': 'XXX',
            'attack': 'XXX',
            'defense': 'XXX',
            'health': 'XXX',
            'mana': 'XXX',
            'luck': 'XXX'
        }
    # return redirect('show_profile', id=player.id)
    # return checkAuth(request, redirect('show_profile', id=player.id), player.id)
    return checkAuth(request, render(request, 'player/show.html', { 'player': player }), player.id)

def delete(request):
    return