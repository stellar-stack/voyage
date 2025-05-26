from django.shortcuts import render
from .models import Room
# foot is our base app.

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'Lets learn Calculus'},
#     {'id':3, 'name':'Lets learn Algebra'},
# ]
# creating the methods to render pages.
def Home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'foot/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return  render(request, 'foot/room.html', context)