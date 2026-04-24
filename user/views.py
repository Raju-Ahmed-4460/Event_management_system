from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,Group
from user.forms import RegisterForm,CustomRegistrationForm,CustomLoginForm,AssignRoleForm,CreatGroupForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse

def sign_up(request):
    if request.method =="POST":
        form=CustomRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active=False
            user.save()

            messages.success(request,"Check your email")
            return redirect('login')

    else:
        form=CustomRegistrationForm()

    return render(request,"registration/sign_up.html",{"form":form})



def user_login(request):
    form=CustomLoginForm()
    if request.method=="POST":
        form=CustomLoginForm(data=request.POST)
        if  form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home1')
        messages.error(request,"Login faild")
    return render(request,"registration/login.html",{'form':form})



def Log_out(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    

def Activate_user(request, user_id, token):
    
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
          user.is_active = True
          user.save()
          return redirect('login')
        else:
            return HttpResponse("invalid id or token")
    except User.DoesNotExist:
        return HttpResponse("user not Found")
    


def admin_dashboard(request):
    users=User.objects.all()
    return render(request,'admin/dashboard.html',{'users':users})


def assign_role(request,user_id):
    form=AssignRoleForm()
    user=User.objects.get(id=user_id)

    if request.method=="POST":
        form=AssignRoleForm(request.POST)
        if form.is_valid():
           role=form.cleaned_data.get('role')
           user.groups.clear()
           user.groups.add(role)
           messages.success(request,f"Group added for {user.username} to {role.name}")
           return redirect('admin_dashboard')
        
    return render(request,"admin/assignrole.html",{'form':form})


def  create_group(request):
    form=CreatGroupForm()
    if request.method=="POST":
        form=CreatGroupForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,f"Create {Group.name} sucessfully")
            return redirect('admin_dashboard')

    return render(request,"admin/creategroup.html",{'form':form})


def group_list(request):
    groups=Group.objects.all()

    return render(request,"admin/grouplist.html",{'groups':groups})
    


    
