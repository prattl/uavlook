# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0046_auto_20150505_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusettings',
            name='menu_font_size',
            field=models.CharField(default='1', max_length=4, verbose_name='Menu Font Size', help_text='Specify a font size in rem units. 1 rem is normal text size, use only up to 2 decimal places..'),
            preserve_default=True,
        ),
    ]
