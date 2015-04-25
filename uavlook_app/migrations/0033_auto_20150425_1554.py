# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0032_slideshow_data_transition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='data_transition',
            field=models.CharField(max_length=56, help_text='Type of transition. Default is slide.', null=True, verbose_name='Data Transition', choices=[('slide', 'Slide'), ('crossfade', 'Crossfade (dissolve)')], blank=True),
            preserve_default=True,
        ),
    ]
