from django.shortcuts import render

# foot is our base app.

rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'Lets learn Calculus'},
    {'id':3, 'name':'Lets learn Algebra'},
]
# creating the methods to render pages.
def Home(request):
    context = {'rooms':rooms}
    return render(request, 'foot/home.html', context)

def Room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return  render(request, 'foot/room.html', context)