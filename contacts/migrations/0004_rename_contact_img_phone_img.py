# Generated by Django 5.1.1 on 2024-09-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_phone_contact_img_alter_phone_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='contact_img',
            new_name='img',
        ),
    ]
