from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from accounts.models import UserProfile
from events.models import Event, EventMembers

def get_user(request):
    user = get_object_or_404(UserProfile, user=request.user)
    return user

def get_events(request):
    user = get_user(request)
    # Use filter() instead of get() to handle cases where there are no events
    fetch_events = Event.objects.filter(creator=user)
    if fetch_events.exists():  # Check if any events exist
        events = {
            'fetch_events': fetch_events,  # Pass the queryset directly
        }
    else:
        #events = "You have no events"  # Or, better, an empty queryset
        events = fetch_events #This returns an empty queryset which is better than a string.
    return events

def home(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    user = get_user(request)
    events = get_events(request)
    print(f"Username is {user}")
    print(f"{events}")
    # Access events in your template:
    # {% if events.fetch_events %}
    #     {% for event in events.fetch_events %}
    #         {{ event.event_name }} - {{ event.date_time }}<br>
    #     {% endfor %}
    # {% else %}
    #     {{ events }}  (Or handle the no-events case gracefully)
    # {% endif %}
    return render(request, 'home/index.html', {'events': events}) # Pass 'events' to the template




