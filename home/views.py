from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import UserProfile
from events.models import Event, EventItem

def get_user(request):
    user = get_object_or_404(UserProfile, user=request.user)
    return user

def home(request, event_detail):
    if not request.user.is_authenticated:
        return redirect('account_login')  # Redirect to login if not logged in
    # Otherwise, handle the logged-in case (e.g., show a welcome page)
    context = {'event_detail': event_detail}
    return render(request, 'home/index.html', context)

def events(request, user):    
    try:
        events = get_object_or_404(Events, user_profile=user)
        for event in events:
            print(event.event_name, event.event_id, event.date_time)                    
    except Events.DoesNotExist:
        events = None
    event_items = events.lineitems.all()
    template = 'account/order_history.html'
    context = {
        'event': event,       
    }
    return event_detail



