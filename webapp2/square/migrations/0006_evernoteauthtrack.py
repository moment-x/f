# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('square', '0005_auto_20150907_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='EverNoteAuthTrack',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('oauth_token', models.CharField(max_length=1000, null=True)),
                ('oauth_token_secret', models.CharField(max_length=1000, null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
