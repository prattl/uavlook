# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0036_backgroundpicture_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundpicture',
            name='header_logo',
            field=models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, blank=True, null=True, verbose_name='Logo Image'),
            preserve_default=True,
        ),
    ]
