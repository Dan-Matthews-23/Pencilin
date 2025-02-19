from django.db import models
from accounts.models import UserProfile
import uuid
import datetime


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='event')    
    name = models.CharField(max_length=100,
                                    null=False, default="Test")
    description = models.CharField(max_length=2000, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_event =  models.DateField(auto_now_add=True)#auto_now_add=True)    

    def __str__(self):
        return self.name


class EventMembers(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                               related_name='items')
    member = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='member_profile')    
    date_invited = models.DateField(auto_now_add=True)
    accepted =  models.BooleanField(null=True, blank=True)