# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0047_auto_20150508_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentsection',
            name='classname',
            field=models.CharField(blank=True, verbose_name='CSS Class Name', max_length=240, null=True),
            preserve_default=True,
        ),
    ]
