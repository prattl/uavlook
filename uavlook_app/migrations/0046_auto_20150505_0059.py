# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0045_remove_menusettings_menu_font_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='data_allowfullscreen',
            field=models.BooleanField(help_text='Check to display an icon in the top right corner to allow the image to display full screen when clicked.', verbose_name='Data Allow Fullscreen', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='data_stopautoplayontouch',
            field=models.BooleanField(help_text='Check this to make the slideshow stop autoplaying when clicked or touched.', verbose_name='Data Stop Autoplay On Touch', default=True),
            preserve_default=True,
        ),
    ]
