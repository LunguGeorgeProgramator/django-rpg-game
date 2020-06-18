from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('arena', views.index, name='battle_arena'),
]