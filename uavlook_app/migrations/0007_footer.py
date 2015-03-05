# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0006_auto_20150304_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', auto_created=True, serialize=False, parent_link=True)),
                ('title', models.CharField(verbose_name='title', max_length=240, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
