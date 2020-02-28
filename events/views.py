from django.shortcuts import render
from .models import Event

# Create your views here.

def all_events(request):
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})