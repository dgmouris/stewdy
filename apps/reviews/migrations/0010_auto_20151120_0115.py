# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20151120_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 1, 15, 15, 629556), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 1, 15, 15, 629678), auto_now=True),
            preserve_default=True,
        ),
    ]
