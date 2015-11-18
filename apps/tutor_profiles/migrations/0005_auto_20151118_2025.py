# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_profiles', '0004_auto_20151118_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorreviews',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 25, 59, 186049), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorreviews',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 25, 59, 186090), auto_now=True),
            preserve_default=True,
        ),
    ]
