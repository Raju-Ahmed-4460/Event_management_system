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
    password1=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','confirm_password']
    def clean_password1(self):
            password1=self.cleaned_data.get('password1')
            errors=[]
            if len(password1) <8:
                errors.append("Password must be at least 8 character long")
            if "abc" not in password1:
                errors.append("Password must cotain uppercase lowercase letter and special character")

            if errors:
                 raise forms.ValidationError(errors)
            return password1
    
    def clean(self): # non field error
         cleaned_data=super().clean()
         password1=self.cleaned_data.get("password1")
         confirm_password=self.cleaned_data.get("confirm_password")

         if password1 != confirm_password:
              raise forms.ValidationError("password are not same")
         
         return cleaned_data
    def clean_email(self):
         email=self.cleaned_data.get('email')
         email_exists=User.objects.filter(email=email).exists()

         if email_exists:
              raise  forms.ValidationError("Email already exists")
         return email
              



