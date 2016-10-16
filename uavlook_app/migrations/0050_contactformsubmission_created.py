# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0049_auto_20161016_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformsubmission',
            name='created',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
    ]
