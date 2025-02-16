from django.db import models
from accounts.models import UserProfile
import uuid
import datetime


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='event')    
    event_name = models.CharField(max_length=32,
                                    null=False, editable=False, default="Test")    
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


class EventItem(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                               related_name='items')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='event_item')    
    date_time = models.DateTimeField(auto_now_add=True)