from django.urls import path
from . import views

# making the routes to visit those pages

urlpatterns = [
   
    # after this visit the project(voyage) urls.py
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    

    path('', views.Home, name="home" ),
    path('room/<str:pk>/', views.room, name="room"),  

    path('create-room/', views.createRoom, name="create-room"),
    # THEN GO TO HOME.HTML TO CREATE A LINK (createroom).


    # path to update the form
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]