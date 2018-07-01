from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^regby-rostov/', include('rk_dgtu.urls')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True

urlpatterns += staticfiles_urlpatterns()