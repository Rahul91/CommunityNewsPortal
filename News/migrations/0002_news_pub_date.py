# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 10, 51, 10, 563627, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
