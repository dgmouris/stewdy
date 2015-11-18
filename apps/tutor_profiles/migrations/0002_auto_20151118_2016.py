# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorprofile',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 16, 0, 160166), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 16, 0, 160725), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 16, 0, 160753), auto_now=True),
            preserve_default=True,
        ),
    ]
