# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160602_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(verbose_name='Start'),
        ),
    ]
