from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^news/$', views.news, name='news'),
    url(r'^galary/$', views.galary, name='galary'),
    url(r'^galary/(?P<albom_id>[0-9]+)/$', views.albom, name='albom'),
]
