# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0018_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ImageField(null=True, upload_to=cms.models.pluginmodel.get_plugin_media_path, blank=True, verbose_name='Background iImage'),
            preserve_default=True,
        ),
    ]
