from django.shortcuts import render
from django.http import HttpResponse
#from events.forms import CreateEvent

def events(request):
    return render(request, 'events/index.html')


def render_create_event_form(request):
    form = CreateEvent()
    #basket = request.session.get('basket', {})
    try:
        profile = UserProfile.objects.get(user=request.user)
        form = Event(initial={
                'event_name': profile.full_name,
                #'date_time': profile.user.email,
                'user_profile': user_profile,
                #'postcode': profile.postcode,
                #'town_or_city': profile.town_or_city,
                ##'street_address1': profile.street_address1,
                'street_address2': profile.street_address2,
                #'county': profile.county,
                })
    except UserProfile.DoesNotExist:
        form = CreateEvent()
    form = form
    template = 'events/create_event.html'
    context = {
            #'basket': basket,
            'form': form,
    }
    return render(request, template, context)