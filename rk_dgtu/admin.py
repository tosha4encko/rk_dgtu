from django.contrib import admin
from .models import New, Event, Paragraph, Albom, Photo, Video

class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1
    verbose_name_plural = 'Абзыцы'

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    verbose_name_plural = 'Видео'

class AlbomInline(admin.TabularInline):
    model = Albom
    extra = 1
    verbose_name_plural = 'Альбом'

class ProposalSourceAdmin(admin.ModelAdmin):
    inlines = (ParagraphInline, VideoInline, AlbomInline)

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    verbose_name_plural = 'Фото'


class GalaryAdmin(admin.ModelAdmin):
    inlines = (PhotoInline, )

admin.site.register(Albom, GalaryAdmin)
admin.site.register(New, ProposalSourceAdmin)
admin.site.register(Event)
admin.site.register(Video)