from django.urls import path
from . import views

# making the routes to visit those pages

urlpatterns = [
    # after this visit the project(voyage) urls.py
    path('', views.Home, name="home" ),
    path('room/', views.Room, name="room"),
]