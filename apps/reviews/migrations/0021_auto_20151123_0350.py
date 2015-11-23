# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0020_auto_20151123_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 3, 50, 6, 520735), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 3, 50, 6, 520775), auto_now=True),
            preserve_default=True,
        ),
    ]
