# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0008_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='google_plus',
            field=models.CharField(verbose_name='Google Plus URL', blank=True, max_length=240, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='instagram',
            field=models.CharField(verbose_name='Instagram URL', blank=True, max_length=240, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='twitter',
            field=models.CharField(verbose_name='Twitter URL', blank=True, max_length=240, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='youtube',
            field=models.CharField(verbose_name='Youtube URL', blank=True, max_length=240, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='facebook',
            field=models.CharField(verbose_name='Facebook URL', blank=True, max_length=240, null=True),
            preserve_default=True,
        ),
    ]
