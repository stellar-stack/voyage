from django.shortcuts import render
from django.http import HttpResponse

# foot is our base app.

# creating the methods to render pages.
def Home(request):
    return render(request, 'home.html')

def Room(request):
    return  render(request, 'room.html')