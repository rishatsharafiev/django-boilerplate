"""Urls"""

from conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include(frontend_urls)),
    path('admin/', admin.site.urls),
    path('logger/', include('apps.logger.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
