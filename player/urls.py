from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.index, name='show_players'),
    path('profile/<int:id>', views.show, name='show_profile'),
    path('profile/create', views.create, name='create_profile'),
    path('profile/login', views.login, name='login_profile'),
    path('profile/logout', views.logout, name='logout_profile'),
]