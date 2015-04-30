# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0039_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundpicture',
            name='header',
        ),
    ]
