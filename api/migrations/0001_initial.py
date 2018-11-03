# Generated by Django 2.1.2 on 2018-11-02 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('start_time', models.CharField(max_length=255)),
                ('end_time', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('free_food', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('url', models.SlugField(null=True, unique=True)),
                ('photo', models.URLField()),
                ('linkedin', models.URLField()),
                ('website', models.URLField()),
                ('github', models.URLField()),
                ('year_joined', models.DateField()),
                ('alumnus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Team')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(to='api.Role'),
        ),
        migrations.AddField(
            model_name='member',
            name='teams',
            field=models.ManyToManyField(to='api.Team'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
