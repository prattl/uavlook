# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
#        ('cms', '0004_auto_20150430_1405'),
        ('uavlook_app', '0040_remove_backgroundpicture_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='Header',
        ),
    ]
