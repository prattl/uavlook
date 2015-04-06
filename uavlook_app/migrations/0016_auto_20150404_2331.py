# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0015_auto_20150322_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slideshowmedia',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='threecolumns',
            name='horizontal',
            field=models.BooleanField(verbose_name='Horizontal', help_text='Check if these columns should be arranged on top of one another horizontally.', default=False),
            preserve_default=True,
        ),
    ]
