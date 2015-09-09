# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('square', '0004_auto_20150829_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquareImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.CharField(null=True, max_length=100)),
                ('cursor', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='square',
            name='image',
        ),
        migrations.AddField(
            model_name='squareimage',
            name='square',
            field=models.ForeignKey(to='square.Square'),
        ),
    ]
