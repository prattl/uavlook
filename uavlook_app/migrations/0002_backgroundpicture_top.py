# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundpicture',
            name='top',
            field=models.BooleanField(default=False, help_text='Check if this image should appear at the top of the page.'),
            preserve_default=True,
        ),
    ]
