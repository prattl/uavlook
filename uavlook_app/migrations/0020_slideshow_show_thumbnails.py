# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0019_homepage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='show_thumbnails',
            field=models.BooleanField(default=True, help_text='Check to display thmbnails below the slideshow.', verbose_name='Show Thumbnails'),
            preserve_default=True,
        ),
    ]
