# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_telegramuser_timezone_offset'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='language',
            field=models.CharField(default='en-us', max_length=8, verbose_name='Language'),
        ),
    ]
