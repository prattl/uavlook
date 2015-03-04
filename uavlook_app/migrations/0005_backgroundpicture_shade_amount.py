# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0004_auto_20150304_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundpicture',
            name='shade_amount',
            field=models.DecimalField(decimal_places=2, help_text='The amount of shading to add to the image. 0.00 is no shading, and 1.00 is all black. Use up to 2 decimal places.', max_digits=3, default=0.0),
            preserve_default=True,
        ),
    ]
