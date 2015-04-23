# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0026_contactform_recipients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactformsubmission',
            name='inquiry_type',
        ),
    ]
