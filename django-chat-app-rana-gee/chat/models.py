# models.py

from django.db import models

class Registratoin(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(Registratoin, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)
