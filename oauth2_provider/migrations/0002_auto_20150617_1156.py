# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesstoken',
            name='application',
        ),
        migrations.RemoveField(
            model_name='accesstoken',
            name='user',
        ),
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='application',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='user',
        ),
        migrations.DeleteModel(
            name='Grant',
        ),
        migrations.RemoveField(
            model_name='refreshtoken',
            name='access_token',
        ),
        migrations.DeleteModel(
            name='AccessToken',
        ),
        migrations.RemoveField(
            model_name='refreshtoken',
            name='application',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.RemoveField(
            model_name='refreshtoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='RefreshToken',
        ),
    ]
