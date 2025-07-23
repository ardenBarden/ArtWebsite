from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/cordial-invite', views.invite, name='cordial-invite'),
    path('/agenda', views.agenda, name='agenda'),
    path('/homeagain', views.homeagain, name='homeagain'),
]