from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Event, Albom

def news(request):
    return render(request, 'rk_dgtu/index.html')

def galary(request):
    alboms = Albom.objects.all()
    events = Event.objects.all()[:2]
    context = {
                'alboms': alboms,
                'events': events
              }

    return render(request, 'rk_dgtu/galary.html', context)

def albom(request, albom_id):
    albom = Albom.objects.get(pk=albom_id)
    events = Event.objects.all()[:2]
    context = {
                'albom': albom,
                'events': events
              }

    return render(request, 'rk_dgtu/albom.html', context)
