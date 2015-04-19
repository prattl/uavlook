# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0021_slideshow_show_arrows'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='data_fit',
            field=models.CharField(help_text='How the images should fit inside the slideshow. See http://fotorama.io/customize/fit/ for more informatioon,', default='contain', max_length=240, verbose_name='Data Fit', choices=[('contain', 'Contain'), ('cover', 'Cover'), ('scaledown', 'Scale Down'), ('none', 'None')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_height',
            field=models.CharField(help_text='Height of the slideshow. Specify a whole number (600) or a percent (100%).', null=True, verbose_name='Data Height', max_length=5, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_ratio',
            field=models.CharField(help_text='Aspect Ratio of the slideshow. Specify either a decimal (1.333) or a fraction (800/600 or 4/3).', null=True, verbose_name='Data Ratio', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideshow',
            name='data_width',
            field=models.CharField(help_text='Width of the slideshow. Specify a whole number (600) or a percent (100%).', null=True, verbose_name='Data Width', max_length=5, blank=True),
            preserve_default=True,
        ),
    ]
