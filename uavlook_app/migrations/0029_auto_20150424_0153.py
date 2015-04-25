# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0028_contactformsubmission_inquiry_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=models.ImageField(verbose_name='Logo Image', upload_to=cms.models.pluginmodel.get_plugin_media_path, blank=True, null=True),
            preserve_default=True,
        ),
    ]
