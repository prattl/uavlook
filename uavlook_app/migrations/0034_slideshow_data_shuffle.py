# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0033_auto_20150425_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='data_shuffle',
            field=models.BooleanField(verbose_name='Data Shuffle', help_text='Check to shuffle the images in a random order when the page loads.', default=False),
            preserve_default=True,
        ),
    ]
