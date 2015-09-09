# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('square', '0003_auto_20150828_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='square',
            name='image',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='square',
            name='paragraph',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='square',
            name='title',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
