# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0003_contentsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentsection',
            name='center',
            field=models.BooleanField(help_text='Check if the contents of this section should be centered. If not, they will be left-justified.', default=False, verbose_name='center'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contentsection',
            name='header',
            field=models.CharField(null=True, max_length=240, verbose_name='header', blank=True),
            preserve_default=True,
        ),
    ]
