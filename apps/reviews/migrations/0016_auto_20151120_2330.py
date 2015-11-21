# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_auto_20151120_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorprofile',
            name='education',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='slug',
            field=models.SlugField(max_length=40, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='slug',
            field=models.SlugField(max_length=40, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 23, 30, 4, 512806), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 23, 30, 4, 512847), auto_now=True),
            preserve_default=True,
        ),
    ]
