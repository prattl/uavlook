# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0048_contentsection_classname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformsubmission',
            name='message',
            field=models.TextField(null=True, max_length=2400, verbose_name='Message', blank=True),
            preserve_default=True,
        ),
    ]
