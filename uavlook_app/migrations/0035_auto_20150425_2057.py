# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0034_slideshow_data_shuffle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='data_stopautoplayontouch',
            field=models.BooleanField(verbose_name='Data Stop Autoplay On Touch', help_text='Uncheck this to enable autoplay on touch devices (if a number was entered above). By default, autoplay is not enabled on touch devices.', default=True),
            preserve_default=True,
        ),
    ]
