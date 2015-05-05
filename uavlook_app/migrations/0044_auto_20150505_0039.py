# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0043_menusettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menusettings',
            options={'verbose_name': 'Menu Settings', 'verbose_name_plural': 'Menu Settings'},
        ),
        migrations.AlterField(
            model_name='menusettings',
            name='menu_font_color',
            field=models.CharField(default='000000', verbose_name='Menu Font Color', max_length=6, help_text='Enter a 6 digit color hex code.'),
            preserve_default=True,
        ),
    ]
