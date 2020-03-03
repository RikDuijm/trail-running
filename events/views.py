from django.shortcuts import render
from django.views.generic import ListView
from .models import Month, Event
from django.utils import timezone

# Create your views here.
def all_events(request):
    months = Month.objects.all()
    events = Event.objects.all().order_by('date')
    return render(request, "events.html", {"months": months}, {"events": events})

def events_ordered_by_date(request):
    events = Event.objects.all().order_by('date')
    return render(request, "eventsbydate.html", {"events": events})