from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='news'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news/(?P<new_id>[0-9]+)/$', views.new, name='news'),
    url(r'^galary/photo/$', views.galary, name='news'),
    url(r'^galary/photo/(?P<albom_id>[0-9]+)/$', views.photo, name='albom'),
    url(r'^galary/video/$', views.video, name='video'),
]
