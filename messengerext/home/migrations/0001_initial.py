# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-19 19:01
from __future__ import unicode_literals

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
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'verbose_name': 'Album',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('duration_sec', models.PositiveIntegerField(blank=True, null=True, verbose_name='DurationSeconds')),
            ],
            options={
                'verbose_name_plural': 'Audios',
                'verbose_name': 'Audio',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('doc_type', models.CharField(max_length=10, verbose_name='Type')),
            ],
            options={
                'verbose_name_plural': 'Files',
                'verbose_name': 'File',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('picture', models.FileField(blank=True, null=True, upload_to='', verbose_name='Picture')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('url', models.URLField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Links',
                'verbose_name': 'Link',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('resolution', models.CharField(blank=True, max_length=30, null=True, verbose_name='Resolution')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='', verbose_name='Thumbnail')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
            },
        ),
        migrations.CreateModel(
            name='TelegramLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField(verbose_name='JSON')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('content', models.TextField(verbose_name='Content')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Texts',
                'verbose_name': 'Text',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('duration_sec', models.PositiveIntegerField(blank=True, null=True, verbose_name='DurationSeconds')),
                ('resolution', models.CharField(blank=True, max_length=30, null=True, verbose_name='Resolution')),
                ('thumbnail', models.FileField(upload_to='', verbose_name='Thumbnail')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.AddField(
            model_name='file',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group'),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='audio',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group'),
        ),
        migrations.AddField(
            model_name='audio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='home.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='videos',
            field=models.ManyToManyField(to='home.Video'),
        ),
    ]
