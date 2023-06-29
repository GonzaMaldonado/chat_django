from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Room, Message

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


def roomView(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    }) 
    #template_name = 'room.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        context['room'] = kwargs['room']
        context['room_details'] = Room.objects.get(name=kwargs['room'])
        return context



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

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room = int(request.POST['room_id'])
    
    room_id = Room.objects.get(id=room)

    print(room_id)

    new_message = Message.objects.create(body=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})