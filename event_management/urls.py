

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("event/", include('event.urls')),
    path("user/", include('user.urls')),
    path("core/", include('core.urls')),
]

# Only enable debug toolbar in DEBUG mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
