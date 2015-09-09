# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('square', '0007_evernoteauthtrack_oauth_verifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squareimage',
            name='square',
        ),
        migrations.AddField(
            model_name='square',
            name='image',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='SquareImage',
        ),
    ]
