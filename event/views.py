from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.form import EventModelForm,CategoryModelForm,ParticipantModelForm
from event.models import Event,Participant,Category
from  datetime import date,time


# Create your views here.
def Event_form(request):
    form=EventModelForm()

    if request.method=="POST":
        form=EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Add Sucessfully")

    context={
        "form":form
    }
    return render(request,"dashboard/form.html",context)





# create category form

def Category_form(request):
    form=CategoryModelForm()

    if request.method=="POST":
        form=CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Add Sucessfully")

    context={
        "form":form
    }
    return render(request,"dashboard/form.html",context)






# create Participent form
def Participent_form(request):
    form=ParticipantModelForm()

    if request.method=="POST":
        form=ParticipantModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Add Sucessfully")

    context={
        "form":form
    }
    return render(request,"dashboard/form.html",context)




def dashboard(request):
    type=request.GET.get('type','all')
    
    today = date.today()
    base_query=Event.objects.select_related('category')\
                           .prefetch_related('participants')
    events = base_query.all()

    total_events = base_query.count()
    total_participants = Participant.objects.count()

    upcoming = base_query.filter(date__gt=today).count()
    past = base_query.filter(date__lt=today).count()

    today_events = base_query.filter(date=today)

    


    

    if type=='total_events':
        events=base_query.all()

    elif type=='past':
        events=base_query.filter(date__lt=today)
    
    elif type=='upcoming':
        events=base_query.filter(date__gt=today)
    elif type=='total_participants':
        events=Participant.objects.all()
    elif type=='all':
        events=base_query.all()





    context = {
        'events': events,
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming': upcoming,
        'past': past,
        'today_events': today_events,
    }
    


    return render(request, 'dashboard/dashboard.html', context)

    



