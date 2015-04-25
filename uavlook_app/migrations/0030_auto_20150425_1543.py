# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0029_auto_20150424_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='data_autoplay',
            field=models.IntegerField(help_text='Enter a number here to enable auto-play. Enter the number of milliseconds to specify how long each image should appear. For example, for 5 seconds enter 5000.', null=True, blank=True, verbose_name='Data Autoplay'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_loop',
            field=models.BooleanField(help_text='Check this to loop to the beginning of the slideshow when the end is reached.', default=False, verbose_name='Data Loop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_stopautoplayontouch',
            field=models.BooleanField(help_text='Check this to enable autoplay on touch devices (if a number was entered above). By default, autoplay is not enabled on touch devices.', default=True, verbose_name='Data Stop Autoplay On Touch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_transitionduration',
            field=models.IntegerField(help_text='Enter a number to control the duration of the transition effect in milliseconds. For example to fade to the next image in 0.5 seconds, enter 500.', null=True, blank=True, verbose_name='Data Transition Duration'),
            preserve_default=True,
        ),
    ]
