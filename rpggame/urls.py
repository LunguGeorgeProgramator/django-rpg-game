from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_index'),
    path('', include('player.urls')),
    path('', include('arena.urls')),
    path('', include('engine.urls')),
]
