# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0044_auto_20150505_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menusettings',
            name='menu_font_color',
        ),
    ]
