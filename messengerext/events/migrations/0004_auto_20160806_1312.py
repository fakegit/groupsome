# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 13:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='maybe', max_length=8, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Attending',
                'verbose_name_plural': 'Attending',
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
        migrations.AddField(
            model_name='attending',
            name='event',
            field=models.ManyToManyField(related_name='attending', to='events.Event'),
        ),
        migrations.AddField(
            model_name='attending',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
