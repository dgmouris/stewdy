# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20151120_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='slug',
            field=models.SlugField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorprofile',
            name='slug',
            field=models.SlugField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 23, 18, 58, 590057), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 23, 18, 58, 590095), auto_now=True),
            preserve_default=True,
        ),
    ]
