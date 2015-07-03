# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20150701_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(max_length=100),
        ),
    ]
