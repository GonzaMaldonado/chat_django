from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Room, Message

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


class Room(TemplateView):
    template_name = 'room.html'


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(f'/{room}/?username={username}')
    else:
      new_room = Room.objects.create(name=room)
      new_room.save()
      return redirect(f'/{room}/?username={username}')
    
    #'/+room+/?username=+username'