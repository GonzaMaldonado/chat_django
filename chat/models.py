from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
      return self.name

class Message(models.Model):
    body = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=500)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
       return self.body