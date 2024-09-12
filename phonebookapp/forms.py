from django import forms
from phonebookapp.models import Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PhoneForm(forms.ModelForm):
    mobile=PhoneNumberField(region='IN')
    class Meta:
        model=Contact
        fields=['name','email','img']

class UserRegistratonForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','password1','password2']