# Generated by Django 3.0.6 on 2020-09-02 11:53

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("accounts", "0006_auto_20200818_2141")]

    operations = [
        migrations.AlterField(
            model_name="phonenumbermodel",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, default=None, max_length=128, region=None, unique=True
            ),
        )
    ]
