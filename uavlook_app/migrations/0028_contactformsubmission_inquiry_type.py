# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0027_remove_contactformsubmission_inquiry_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformsubmission',
            name='inquiry_type',
            field=models.ForeignKey(to='uavlook_app.InquiryType', default=''),
            preserve_default=False,
        ),
    ]
