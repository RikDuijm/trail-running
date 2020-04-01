from django.shortcuts import render
from django.views.generic import ListView
from .models import Month, Event
from django.utils import timezone
from django.db.models import Q 

# Create your views here.
def all_events(request):  
    events = Event.objects.all()
#    months = Month.objects.all()
    return render(request, "events.html", {"events": events})  # {"months": months}, 

def search_race_name(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q1 = request.GET.get('q1')
    events = Event.objects.filter(
        Q(name__icontains=q1))
    return render(request, "events.html", {"events": events})


def search_race_month(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q2 = request.GET.get('q2')
    events = Event.objects.filter(
        Q(month__icontains=q2))
    return render(request, "events.html", {"events": events}) 
    

def search_race_distance(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q3 = request.GET.get('q3')
    events = Event.objects.filter(
        Q(distance_range__icontains=q3))
    return render(request, "events.html", {"events": events}) 
    

def search_race_region(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q4 = request.GET.get('q4')
    events = Event.objects.filter(
        Q(region__icontains=q4))
    return render(request, "events.html", {"events": events})
