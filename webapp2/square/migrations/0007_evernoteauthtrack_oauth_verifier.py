# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('square', '0006_evernoteauthtrack'),
    ]

    operations = [
        migrations.AddField(
            model_name='evernoteauthtrack',
            name='oauth_verifier',
            field=models.CharField(null=True, max_length=1000),
        ),
    ]
