from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.


def events(request):
    events = Event.objects.all()
    for event in events:
        event.participants_count = event.participants.count()
    message="Мероприятия"
    return render(request,"events.html",{
        'title':message,
        'event_list':events})

def home(request):
    return render(request,"home.html")


def events_by_date(request, date):
    events = Event.objects.filter(planned_date=date).order_by('-planned_date')
    for event in events:
        event.participants_count = event.participants.count()
    return render(request, 'events_by_date.html', {
        'events': events,
        'date': date
    })

def event_participants(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participants = event.eventparticipation_set.select_related('user').all()
    
    return render(request, 'event_participants.html', {
        'event': event,
        'participants': participants
    })

def event_types(request):
    types = Event.objects.values_list('event_type', flat=True ).distinct()
    
    return render(request, 'event_types.html', {
        'types': types
    })

def events_by_type(request, type):
    events = Event.objects.filter(event_type=type).order_by('-planned_date')
    for event in events:
        event.participants_count = event.participants.count()
    return render(request, 'events_by_type.html', {
        'events': events,
        'event_type': type
    })

def detail(request,event_id):
     event = get_object_or_404(Event, id=event_id)

     return render(request, 'detail.html', {
        'event': event,
    })

