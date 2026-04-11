from django.urls import path
from event.views import Event_form,Category_form,Participent_form

urlpatterns = [
    path("create_event/",Event_form),
    path("create_category",Category_form),
    path("participent_create/",Participent_form),
    
]
