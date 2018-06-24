from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Event, Albom

def news(request):
    events = Event.objects.all().order_by('-pub_date')[:2]
    news    = News.objects.all().order_by('-pub_date')[:3]
    return render(request, 'rk_dgtu/index.html', {'news': news, 'events': events})

def galary(request):
    alboms = Albom.objects.all().order_by('-pub_date')
    return render(request, 'rk_dgtu/index.html', {'alboms': alboms})

def albom(request, albom_id):
    photo = Albom.objects.get(pk=albom_id).photo_set.all()
    return render(request, 'rk_dgtu/index.html', {'photo': photo})
