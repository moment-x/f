# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(max_length=150)),
                ('owner', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='thirdpartyuser',
            name='owner',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(null=True, max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='friend',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friend_rel_+'),
        ),
        migrations.AddField(
            model_name='user',
            name='friend_request',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friend_request_rel_+'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(null=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(null=True, max_length=15),
        ),
        migrations.DeleteModel(
            name='ThirdPartyUser',
        ),
    ]
