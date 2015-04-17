# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0020_slideshow_show_thumbnails'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='show_arrows',
            field=models.CharField(choices=[('always', 'Always display arrows'), ('true', 'Display arrows on hover'), ('false', 'Never display arrows')], verbose_name='Navigation Arrows', max_length=240, help_text='Navigation Arrows', default='true'),
            preserve_default=True,
        ),
    ]
