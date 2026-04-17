from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)

        self.fields['username'].help_text=None
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None


class CustomRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
    
    def clean(self): # non field error
         cleaned_data=super().clean()
         p1=cleaned_data.get("password")
         p2=cleaned_data.get("confirm_password")

         if p1 and p2 and p1!=p2:
              raise forms.ValidationError("password are not same")
         
         return cleaned_data
    def clean_email(self):
         email=self.cleaned_data.get('email')
         email_exists=User.objects.filter(email=email).exists()

         if email_exists:
              raise  forms.ValidationError("Email already exists")
         return email
              



