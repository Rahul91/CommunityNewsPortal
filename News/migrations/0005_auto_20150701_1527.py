# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_auto_20150701_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='upvote',
            field=models.IntegerField(default=1),
        ),
    ]
