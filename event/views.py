from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.form import EventModelForm,CategoryModelForm,ParticipantModelForm


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

    



