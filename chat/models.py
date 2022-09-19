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


class Notifications(models.Model):
    user_sender=models.ForeignKey(NewUser,null=True,blank=True,related_name='user_sender',on_delete=models.CASCADE)
    user_revoker=models.ForeignKey(NewUser,null=True,blank=True,related_name='user_revoker',on_delete=models.CASCADE)
    status=models.CharField(max_length=264,null=True,blank=True,default="unread")
    type_of_notification=models.CharField(max_length=264,null=True,blank=True)           





    



