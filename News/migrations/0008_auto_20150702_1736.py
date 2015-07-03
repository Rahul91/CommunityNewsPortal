# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_auto_20150702_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default=b'title', max_length=150),
        ),
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='news',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
