from django.shortcuts import render
from django.views.generic import ListView
from .models import Month, Event

# Create your views here.



# def all_events(request):
#     months = Month.objects.all()
#     events = Event.objects.all()
#     return render(request, "events.html", {"months": months}, {"events": events})


class Calendar(ListView):
    template_name = "events.html"
    queryset = Month.objects.all()

def all_events(self, *args, **kwargs):
    context = Month().all_events(*args, **kwargs)
    context['months'] = Month.objects.all()
    context['events'] = Event.objects.all()
    return context
