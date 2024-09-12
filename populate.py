import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Phonebook.settings')
import phonenumbers
import django
django.setup()
from contacts.models import phone
from faker import Faker
fake=Faker()
mobile=Faker(['en_IN'])
def populate():
    name=fake.name()
    email=fake.email()
    mobile_number=mobile.phone_number()
    contact=phone.objects.get_or_create(name=name,email=email,mobile=mobile_number)
    return contact
def creating(n):
    for i in range(1,n):
        populate()
        print(i,'created')
print('creating')
creating(10)
print('completed')