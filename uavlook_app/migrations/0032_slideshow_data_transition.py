# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0031_auto_20150425_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='data_transition',
            field=models.CharField(max_length=56, null=True, verbose_name='Data Transition', help_text='Type of transition. Default is slide.', blank=True),
            preserve_default=True,
        ),
    ]
