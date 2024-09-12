from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Create your models here.
class Contact(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=PhoneNumberField()
    img=models.ImageField(upload_to='profile_pics',default='contact.jpg')

    def __str__(self):
        return self.name    