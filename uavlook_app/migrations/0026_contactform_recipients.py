# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uavlook_app', '0025_remove_contactform_recipients'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='recipients',
            field=models.ManyToManyField(help_text='Recipients to send contact emails to.', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
