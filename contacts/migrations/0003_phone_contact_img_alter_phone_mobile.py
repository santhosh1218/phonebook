# Generated by Django 5.1.1 on 2024-09-11 08:10

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_phone_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='contact_img',
            field=models.ImageField(default='contact.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
