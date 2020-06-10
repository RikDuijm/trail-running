from django.shortcuts import render
from django.views.generic import ListView
from .models import Event
from django.utils import timezone
from django.db.models import Q 

# Create your views here.
def all_events(request):
    """
    View that renders the empty events page.
    """  
    return render(request, "events.html") 

def search_race_name(request):
    """
    View that will filter the events based on the race name
    """
    q1 = request.GET.get('q1')
    events = Event.objects.filter(
        Q(name__icontains=q1))
    return render(request, "events.html", {"events": events})


def search_race_month(request):
    """
    View that will filter the events based on the month
    """
    q2 = request.GET.get('q2')
    events = Event.objects.filter(
        Q(month__icontains=q2))
    return render(request, "events.html", {"events": events}) 
    

def search_race_distance(request):
    """
    View that will filter the events based on the distance
    """
    q3 = request.GET.get('q3')
    events = Event.objects.filter(
        Q(distance_range__icontains=q3))
    return render(request, "events.html", {"events": events}) 
    

def search_race_region(request):
    """
    View that will filter the events based on the region
    """
    q4 = request.GET.get('q4')
    events = Event.objects.filter(
        Q(region__icontains=q4))
    return render(request, "events.html", {"events": events})
