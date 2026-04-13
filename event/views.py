from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.form import EventModelForm,CategoryModelForm,ParticipantModelForm
from event.models import Event,Participant,Category
from  datetime import date,time
from django.contrib import messages


# Create your views here.
def Event_form(request):
    form=EventModelForm()

    if request.method=="POST":
        form=EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Event added sucessfully")
            return redirect('Event_form')

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
            messages.success(request,"Category added sucessfully")
            return redirect('Category_form')

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
            messages.success(request,"Participent added sucessfully")
            return redirect('Participent_form')
        

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

    events = None
    participants = None
    today_events = None
    mode = 'events'


    if type == 'total_events':
        events = base_query.all()
        mode = 'events'

    elif type == 'past':
        events = base_query.filter(date__lt=today)
        mode = 'events'

    elif type == 'upcoming':
        events = base_query.filter(date__gt=today)
        mode = 'events'

    elif type == 'total_participants':
        participants = Participant.objects.all()
        mode = 'participants'

    elif type == 'today':
        today_events = base_query.filter(date=today)
        mode = 'today'

    else:
        events = base_query.all()
        mode = 'events'

    context = {
        'events': events,
        'participants': participants,
        'today_events': today_events,
        'mode': mode,

        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming': upcoming,
        'past': past,
    }

    return render(request, 'dashboard/dashboard.html', context)




def Update_event_form(request,id):

    event=Event.objects.get(id=id)
    form=EventModelForm(instance=event)

    if request.method=="POST":
        form=EventModelForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,"Event Update sucessfully")
            return redirect('dashboard')

    context={
        "form":form
    }
    return render(request,"dashboard/form.html",context)



def delete_event(request,id):
    if request.method=="POST":
        event=Event.objects.get(id=id)
        event.delete()
        messages.success(request,"Event deleted sucessfully")
        return redirect('dashboard')
    else:
        messages.error(request,"Somthing went wrong")
        return redirect('dashboard')






def Update_Participents_form(request,id):

    event=Participant.objects.get(id=id)
    form=ParticipantModelForm(instance=event)

    if request.method=="POST":
        form=ParticipantModelForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,"Participents Update sucessfully")
            return redirect('dashboard')

    context={
        "form":form
    }
    return render(request,"dashboard/form.html",context)





def delete_participents(request,id):
    if request.method=="POST":
        event=Participant.objects.get(id=id)
        event.delete()
        messages.success(request,"Participents deleted sucessfully")
        return redirect('dashboard')
    else:
        messages.error(request,"Somthing went wrong")
        return redirect('dashboard')

    


def Home(request):
    return render(request,'dashboard/Home.html')


