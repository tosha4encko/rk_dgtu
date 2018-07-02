from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import New, Event, Albom, Video

def home(request):
    events = Event.objects.all().order_by('-pub_date')[:2]

    alboms = Albom.objects.all().order_by('-pub_date')
    news  = New.objects.all().order_by('-pub_date')[:3]
    videos = Video.objects.all()[:4]
    return render(request, 'rk_dgtu/index.html',
                  {'active_albom': alboms[0],
                   'h_alboms': alboms[1:],
                   'news': news, 'videos': videos,
                   'events': events})

def news(request):
    events = Event.objects.all().order_by('-pub_date')[:2]

    news = New.objects.all().order_by('-pub_date')[:5]
    return render(request, 'rk_dgtu/index.html', {'news': news, 'events': events})

def new(request, new_id):
    events = Event.objects.all().order_by('-pub_date')[:2]

    new = New.objects.get(pk=new_id)
    return render(request, 'rk_dgtu/index.html', {'new': new, 'events': events})

def galary(request):
    events = Event.objects.all().order_by('-pub_date')[:2]
    alboms = Albom.objects.all().order_by('-pub_date')
    return render(request, 'rk_dgtu/index.html', {'alboms': alboms, 'events': events})

def photo(request, albom_id):
    events = Event.objects.all().order_by('-pub_date')[:2]
    photo = Albom.objects.get(pk=albom_id).photo_set.all()
    return render(request, 'rk_dgtu/index.html', {'photo': photo, 'events': events})

def video(request):
    events = Event.objects.all().order_by('-pub_date')[:2]
    videos = Video.objects.all()
    return render(request, 'rk_dgtu/index.html', {'videos': videos, 'events': events})

def club(request):
    events = Event.objects.all().order_by('-pub_date')[:2]
    return render(request, 'rk_dgtu/index.html', {'club': 'dgtu', 'events': events})
