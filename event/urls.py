from django.urls import path
from event.views import home

urlpatterns = [
    path("User-dashboard/",home)
]
