from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Event, Albom

def news(request):
    news    = News.objects.all().order_by('pub_date')[:3]
    events  = Event.objects.all().order_by('pub_date')[:2]
    return render(request, 'rk_dgtu/index.html', {'news': news, 'events': events})

def galary(request):
    alboms = Albom.objects.all().order_by('pub_date')
    events = Event.objects.all().order_by('pub_date')[:2]
    context = {
                'alboms': alboms,
                'events': events
              }

    return render(request, 'rk_dgtu/index.html', context)

def albom(request, albom_id):
    albom = Albom.objects.get(pk=albom_id)
    events = Event.objects.all()[:2]
    context = {
                'albom': albom,
                'events': events
              }

    return render(request, 'rk_dgtu/index.html', context)
