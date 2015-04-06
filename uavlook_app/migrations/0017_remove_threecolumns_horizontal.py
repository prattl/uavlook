# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0016_auto_20150404_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threecolumns',
            name='horizontal',
        ),
    ]
