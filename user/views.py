from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.forms import RegisterForm,CustomRegistrationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def sign_up(request):
    if request.method =="POST":
        form=CustomRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request," User Registration sucessfull")

    else:
        form=CustomRegistrationForm()
    

    return render(request,"registration/sign_up.html",{"form":form})



def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home1')
        else:
            messages.error(request,"Login faild")

        
    return render(request,"registration/login.html")



def Log_out(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    
