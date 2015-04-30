# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0037_backgroundpicture_header_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundpicture',
            name='logo_width',
            field=models.IntegerField(help_text='Width of the logo image measured in px. The height will automatically scale with the width.', verbose_name='Logo Width', default='500'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo_width',
            field=models.IntegerField(help_text='Width of the logo image measured in px. The height will automatically scale with the width.', verbose_name='Logo Width', default='500'),
            preserve_default=True,
        ),
    ]
