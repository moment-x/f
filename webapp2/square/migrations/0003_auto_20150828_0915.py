# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('square', '0002_auto_20150824_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliverySquare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='square',
            name='active',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='deliverysquare',
            name='square',
            field=models.ForeignKey(to='square.Square'),
        ),
    ]
