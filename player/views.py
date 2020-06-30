from django.shortcuts import render, redirect
from player.forms import RegisterPlayerForm, LoginPlayerForm
from django.core.exceptions import ObjectDoesNotExist
from player.models import Player, Skills
from engine.core_class import check
from django.contrib.sessions.backends.db import SessionStore


def checkAuth(request, template = None, player_id = None):
    try:
        try:
            player = Player.objects.get(id=player_id)
        except ObjectDoesNotExist:
            return redirect('logout_profile')
        if request.session['player_id'] == player.id:
            return template
        else: 
            return redirect('logout_profile')
    except KeyError:
        return redirect('logout_profile')

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
    player = Player(
        nume = create_form_player.cleaned_data.get('nume'), 
        prenume = create_form_player.cleaned_data.get('prenume'), 
        nume_utilizator = create_form_player.cleaned_data.get('nume_utilizator'), 
        email = create_form_player.cleaned_data.get('email'),
        level = 1,
        experienta = 1,
        attack = 1,
        defense = 1,
        health = 1,
        mana = 1,
        luck = 1,
    )
    try:
        skill = Skills.objects.get(nume='Slash attack2')
    except ObjectDoesNotExist:
        skill = Skills(
            nume = 'Slash attack',
            descriere = 'A simple attack skill, player throws a punch.',
            tip = 'Fighter',
            puncte = 1,
            level_necesar = 1,
            caracteristica_necesara = 'attack',
            caracteristica_puncte_necesare = 1,
        )
        skill.save()
    player.save()
    skill.players.add(player)
    createPlayerSession(request, player)
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
    return redirect('login_profile')

def createPlayerSession(request, player):
    try:
        request.session['player_id'] = player.id
    except KeyError:
        s = SessionStore()
        s['player_id'] = player.id
        s.create()
        s.session_key
        s = SessionStore(session_key=s.session_key)

@check
def login(request):
    player = None
    error = ''
    if request.method == 'POST':
        login_form_player = LoginPlayerForm(request.POST)
        if login_form_player.is_valid():
            user_name = login_form_player.cleaned_data.get('nume_utilizator')
            player = Player.objects.get(
                nume_utilizator = user_name, 
                email = login_form_player.cleaned_data.get('email')
            )
            if player:
                createPlayerSession(request, player)
                return redirect('show_profile', id=player.id)
            else:
                error = 'Nu exista userul ' +  user_name
    else:
        login_form_player = LoginPlayerForm(request.GET or None)
    return render(request, 'player/login.html',{
        'login_form_player': login_form_player,
        'error': error 
    })

@check
def show(request, id):
    player = Player.objects.get(id=id)
    skills = player.skills_set.all()
    return checkAuth(request, render(request, 'player/show.html', { 'player': player, 'skills': skills}), player.id)

def delete(request, id):
    player_to_remove = Player.objects.filter(id=id)
    player_to_remove.delete()
    return checkAuth(request, redirect('login_profile') , id)