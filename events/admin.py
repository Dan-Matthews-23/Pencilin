from django.contrib import admin
from .models import Event, EventMembers

class EventAdmin(admin.ModelAdmin):
    model = Event   
    list_display = (
        'id', 
        'creator', 
        'name', 
        'description',
        'date_created',
        'date_event',
        )
    #ordering = ('-id',)


class EventMembersAdmin(admin.ModelAdmin):
    model = EventMembers
    
    list_display = (
        'event', 
        'member', 
        'date_invited',
        'accepted',
        )



admin.site.register(EventMembers, EventMembersAdmin)
admin.site.register(Event, EventAdmin)

