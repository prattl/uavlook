# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0024_auto_20150419_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='recipients',
        ),
    ]
