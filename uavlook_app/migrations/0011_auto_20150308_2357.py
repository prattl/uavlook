# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0010_blockquote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockquote',
            name='footer',
        ),
        migrations.AddField(
            model_name='blockquote',
            name='attribution',
            field=models.CharField(blank=True, null=True, verbose_name='Attribution', max_length=240),
            preserve_default=True,
        ),
    ]
