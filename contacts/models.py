from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.models import User
#Create your models here
class Phone(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=PhoneNumberField()
    img=models.ImageField(upload_to='profile_pics',default='contact.jpg')

    def __str__(self):
        return self.name    