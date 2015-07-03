# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0010_auto_20150703_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(max_length=300),
        ),
    ]
