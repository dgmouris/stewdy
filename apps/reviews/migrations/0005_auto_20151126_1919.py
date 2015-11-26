# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20151126_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='slug',
            field=models.SlugField(max_length=40, null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorprofile',
            name='slug',
            field=models.SlugField(max_length=40, null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 19, 40, 316727), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 19, 19, 40, 316768), auto_now=True),
            preserve_default=True,
        ),
    ]
