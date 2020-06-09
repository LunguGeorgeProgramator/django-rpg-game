from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re 

from player.models import Player

class LoginPlayerForm(forms.ModelForm):
    email = forms.CharField(
        required=False,
        max_length=25,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introdu adresa ta de email.'
            })
    )
    nume_utilizator = forms.CharField(
        required=False,
        max_length=25,
        label='Nume personaj',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introdu numele caracterului in joc.'
            })
    )
    def clean_email(self):
        email = self.cleaned_data['email']
        if email is None or not email.strip():
            raise ValidationError(_('Campul email nu poate fi gol !!!'))
        if '@' not in email:
            raise ValidationError(_('Campul email trebuie sa contina @ pentru a fi valid !!!'))
        if not re.search(r'\@.+\.\w+$', email):
            raise ValidationError(_('Campul email trebuie sa contina domeniu la final !!!'))
        if re.search(r'^.+\..+\@', email):
            raise ValidationError(_('Campul email nu trebuie sa contina . inainte de @ !!!'))
        return email
    def clean_nume_utilizator(self):
        nume_utilizator = self.cleaned_data['nume_utilizator']
        if nume_utilizator is None or not nume_utilizator.strip():
            raise ValidationError(_('Campul nume personaj nu poate fi gol !!!'))
        return nume_utilizator

    class Meta:
        model = Player
        fields = ('email', 'nume_utilizator')
    

class RegisterPlayerForm(forms.ModelForm):

    # form inputs build
    nume = forms.CharField(
        required=False,
        max_length=25,
        label='Nume',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introdu numele tau.'
            })
    )
    prenume = forms.CharField(
        required=False,
        max_length=25,
        label='Prenume',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introdu prenumele tau.'
            })
    )
    email = forms.CharField(
        required=False,
        max_length=25,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introdu adresa ta de email.'
            })
    )
    nume_utilizator = forms.CharField(
        required=False,
        max_length=25,
        label='Nume personaj',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Introdu numele caracterului in joc.'
            })
    )

    # form restrictions
    def clean_nume(self):
        nume = self.cleaned_data['nume']
        if nume is None or not nume.strip():
            raise ValidationError(_('Campul nume nu poate fi gol !!!'))
        return nume
    def clean_prenume(self):
        prenume = self.cleaned_data['prenume']
        if prenume is None or not prenume.strip():
            raise ValidationError(_('Campul prenume nu poate fi gol !!!'))
        return prenume
    def clean_email(self):
        email = self.cleaned_data['email']
        if email is None or not email.strip():
            raise ValidationError(_('Campul email nu poate fi gol !!!'))
        if '@' not in email:
            raise ValidationError(_('Campul email trebuie sa contina @ pentru a fi valid !!!'))
        if not re.search(r'\@.+\.\w+$', email):
            raise ValidationError(_('Campul email trebuie sa contina domeniu la final !!!'))
        if re.search(r'^.+\..+\@', email):
            raise ValidationError(_('Campul email nu trebuie sa contina . inainte de @ !!!'))
        return email
    def clean_nume_utilizator(self):
        nume_utilizator = self.cleaned_data['nume_utilizator']
        if nume_utilizator is None or not nume_utilizator.strip():
            raise ValidationError(_('Campul nume personaj nu poate fi gol !!!'))
        return nume_utilizator

    class Meta:
        model = Player
        fields = ('nume', 'prenume', 'email', 'nume_utilizator')