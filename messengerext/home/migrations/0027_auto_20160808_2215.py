# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20160801_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='doc_type',
            field=models.CharField(max_length=50, verbose_name='Type'),
        ),
    ]
