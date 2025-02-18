from django.contrib import admin
from .models import Event, EventMembers

class EventMembersAdmin(admin.ModelAdmin):
    model = EventMembers
    #fields = ('event', 'user_profile', 'date_time')
    list_display = ('event', 'user_profile', 'date_time')
    
    

class EventAdmin(admin.ModelAdmin):
    model = Event
    #fields = ('event_id', 'user_profile', 'event_name', 'date_time',)
    list_display = ('event_id', 'user_profile', 'event_name', 'date_time',)
    #ordering = ('-event_id',)



admin.site.register(EventMembers, EventMembersAdmin)
admin.site.register(Event, EventAdmin)


