from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# WEHAVE CREATED 3 MODELS:

# 1. JUST TO HAVE TOPICFIELD TO BE FIELDUP BY USER
class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 2. JUST TO HAVE ROOM FIELD HAVING SEVERAL FIELD
class Room (models.Model):
    # creating ER 
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)


    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# creatign a relationship with Room (one to many)
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.CharField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]