from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.forms import RegisterForm,CustomRegistrationForm

# Create your views here.
def sign_up(request):
    if request.method =="POST":
        form=CustomRegistrationForm(request.POST)
        if form.is_valid():
            # username=form.cleaned_data.get('username')
            # password=form.cleaned_data.get('password1')
            # con_password=form.cleaned_data.get('password2')

            # if password==con_password:
            #     User.objects.create(username=username,password=password)
            # else:
            #     print("password are not same")

            form.save()
    
            
    
    else:
        form=CustomRegistrationForm()
    

    return render(request,"registration/sign_up.html",{"form":form})
    
