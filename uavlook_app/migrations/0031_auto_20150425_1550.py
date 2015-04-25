# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0030_auto_20150425_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='data_click',
            field=models.BooleanField(verbose_name='Data Click', help_text='Check to enable users to click anywhere on the slideshow to advance to the next or previous image. Default is True.', default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_swipe',
            field=models.BooleanField(verbose_name='Data Swipe', help_text='Check to enable users to swipe on the slideshow to advance to the next or previous image. Default is True.', default=True),
            preserve_default=True,
        ),
    ]
