# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160529_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintoken',
            name='host',
            field=models.CharField(max_length=50, null=True, verbose_name='Host'),
        ),
    ]
