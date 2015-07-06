# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News', '0013_auto_20150705_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_news',
            name='title',
        ),
        migrations.RemoveField(
            model_name='user_news',
            name='user',
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user_news',
        ),
    ]
