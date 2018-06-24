# -*- coding: utf-8 -*-
from django.db import models
import datetime

class News(models.Model):
    pub_date = models.DateField(verbose_name='date published')

    real_data = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    photo = models.ImageField(verbose_name='Фото', upload_to='images')
    source = models.URLField(verbose_name='Источник', blank=True)

class Paragraph(models.Model):
    text = models.CharField(max_length=8000)
    news = models.ForeignKey(News, on_delete=models.PROTECT)

class Event(models.Model):
    pub_date = models.DateField(verbose_name='date published')

    real_data = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    ev = models.CharField(verbose_name='Событие', max_length=50)

    comanda_in = models.CharField(max_length=50)
    city_in = models.CharField(max_length=50)
    photo_in = models.ImageField(upload_to='images', null=True, blank=True)
    result_in = models.IntegerField(verbose_name='Положили', blank=True)
    result_out = models.IntegerField(verbose_name='Занесли', blank=True)

    def was_published_recenly(self):
        return self.pub_date >= datetime.now()


class Albom(models.Model):
    pub_date = models.DateField(verbose_name='date published')
    title = models.CharField(max_length=100)
    real_data = models.CharField(max_length=50)

class Photo(models.Model):
    photo = models.ImageField(upload_to='images')
    albom = models.ForeignKey(Albom, on_delete=models.PROTECT)
