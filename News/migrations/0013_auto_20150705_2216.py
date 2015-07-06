# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0012_user_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_news',
            old_name='user_id',
            new_name='user',
        ),
    ]
