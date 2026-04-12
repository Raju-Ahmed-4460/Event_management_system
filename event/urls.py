from django.urls import path
from event.views import Event_form,Category_form,Participent_form,dashboard,Update_event_form,delete_event,Update_Participents_form,delete_participents

urlpatterns = [
    path("create_event/",Event_form,name='Event_form'),
    path("create_category/",Category_form,name="Category_form"),
    path("participent_create/",Participent_form,name='Participent_form'),
    path("dashboard/",dashboard,name="dashboard"),
    path("upadte_event/<int:id>/",Update_event_form,name='update_event'),
    path("delete_event/<int:id>/",delete_event,name='delete_event'),
    path("update_participents/<int:id>/",Update_Participents_form,name='Update_Participents_form'),
    path("delete_participents/<int:id>/",delete_participents,name='delete_participents')
    
]
