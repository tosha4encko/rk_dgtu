from django.contrib import admin
from .models import News, Event, Pararaph, Albom, Photo

class ParagraphInline(admin.TabularInline):
    model = Pararaph
    extra = 1
    verbose_name_plural = 'Абзыцы'

class ProposalSourceAdmin(admin.ModelAdmin):
    inlines = (ParagraphInline, )

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    verbose_name_plural = 'Фото'

class GalaryAdmin(admin.ModelAdmin):
    inlines = (PhotoInline, )

admin.site.register(Albom, GalaryAdmin)
admin.site.register(News, ProposalSourceAdmin)
admin.site.register(Event)