# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20150907_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friend_request',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
