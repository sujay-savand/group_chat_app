import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message, Room

# Create your views here.

@login_required
def show_rooms(request):
    rooms = Room.objects.all()
    return render(request, os.path.join('room', 'rooms.html'), context={'rooms': rooms})

@login_required
def join_room(request, slug):
    individual_room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=individual_room)
    return render(request, os.path.join('room', 'individual_room.html'), context={'room': individual_room, 'messages': messages})
