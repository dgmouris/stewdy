# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_profiles', '0002_auto_20151118_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorprofile',
            name='updated',
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 23, 5, 289442), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 23, 5, 289500), auto_now=True),
            preserve_default=True,
        ),
    ]
