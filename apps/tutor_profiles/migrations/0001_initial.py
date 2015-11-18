# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('specialization', models.TextField(null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 5, 18, 179362), auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TutorReviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('review', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 5, 18, 179941), auto_now_add=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2015, 11, 18, 20, 5, 18, 179968), auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
