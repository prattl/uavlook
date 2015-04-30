# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0035_auto_20150425_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundpicture',
            name='height',
            field=models.DecimalField(max_digits=5, decimal_places=2, help_text='The height of this image measured in rem. 1 rem is about 16px.', default=10.0),
            preserve_default=True,
        ),
    ]
