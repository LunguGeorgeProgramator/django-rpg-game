from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('engine/<int:id>/<int:id_e>', views.engine, name='engine'),
]