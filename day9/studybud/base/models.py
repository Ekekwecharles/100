from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True ) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #Null= true means is can null and blank=true mean when submitting as a form, it can be blank
    # participants =
    updated = models.DateTimeField(auto_now=True) #gets updated whenever save() is called
    created = models.DateTimeField(auto_now_add=True) #Time for when an instance is created

    class Meta:
        # orders the rooms in descending order the updated rooms comes first
        # then the created. When you remove the '-' The order will be in ascending order
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    

class Message(models.Model):
    #one to many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #one to many relationship
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]