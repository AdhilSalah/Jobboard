from django.db import models
from mainuser.models import NewUser

class Room(models.Model):

    sender = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='reciecer')
    room_name = models.CharField(max_length=220,null=True)


    def __str__(self):

        return self.room_name

class Messages(models.Model):

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    message = models.CharField(max_length=225,null=True) 

    def __str__(self):

        return self.room.room_name       





    



