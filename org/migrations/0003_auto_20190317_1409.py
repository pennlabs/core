# Generated by Django 2.1.7 on 2019-03-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0002_auto_20181210_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='job',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
