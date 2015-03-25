# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0014_auto_20150322_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowmedia',
            name='video_url',
            field=models.CharField(blank=True, null=True, verbose_name='URL', help_text='The full URL to a YouTube or Vimeo video page (not embedded URL).', max_length=240),
            preserve_default=True,
        ),
    ]
