

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Event Management System is Running!")

urlpatterns = [
    path("", home),  
    path("admin/", admin.site.urls),
    path("event/", include('event.urls')),
    path("user/", include('user.urls')),
    path("core/", include('core.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
