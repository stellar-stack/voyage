from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Room, Topic
from .form import RoomForm
from django.contrib import messages
# foot is our base app.

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'Lets learn Calculus'},
#     {'id':3, 'name':'Lets learn Algebra'},
# ]
# creating the methods to render pages.

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'username or password does not exist')

    context= {}
    return render(request, 'foot/login_register.html', context)


def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # rooms = Room.objects.all()
    rooms = Room.objects.filter(Q(topic__name__icontains = q) | Q(name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'foot/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return  render(request, 'foot/room.html', context)

# created a methos to request form from room_form.html
# then go to foot/urls.py

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        # print(request.POST)
    context = {'form':form}
    return render(request, 'foot/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'foot/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'foot/delete.html', {'obj':room})