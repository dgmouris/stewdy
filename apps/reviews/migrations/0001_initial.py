# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('education', models.CharField(max_length=200, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('specialization', models.TextField(null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
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
                ('created', models.DateTimeField(default=datetime.datetime(2015, 11, 19, 22, 38, 18, 145383), auto_now_add=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2015, 11, 19, 22, 38, 18, 145420), auto_now=True)),
                ('student', models.ForeignKey(to='reviews.StudentProfile')),
                ('tutor', models.ForeignKey(to='reviews.TutorProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
