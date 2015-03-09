# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0009_auto_20150305_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockQuote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', auto_created=True, parent_link=True, serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, verbose_name='title', blank=True, max_length=240)),
                ('quote', models.TextField(verbose_name='Quote')),
                ('footer', models.CharField(null=True, verbose_name='Footer', blank=True, max_length=240)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
