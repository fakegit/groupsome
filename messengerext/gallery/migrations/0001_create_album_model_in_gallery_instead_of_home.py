# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0022_move_album_and_event_model_to_other_apps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
                ('photos', models.ManyToManyField(to='home.Photo')),
                ('videos', models.ManyToManyField(to='home.Video')),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'verbose_name': 'Album',
            },
        ),
    ]