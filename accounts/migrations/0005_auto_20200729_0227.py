# Generated by Django 3.0.6 on 2020-07-29 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200519_0530'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhoneNumber',
            new_name='PhoneNumberModel',
        ),
    ]
