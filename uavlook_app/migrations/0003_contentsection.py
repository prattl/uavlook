# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0002_backgroundpicture_top'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='cms.CMSPlugin')),
                ('title', models.CharField(verbose_name='title', max_length=240)),
                ('header', models.CharField(verbose_name='title', max_length=240, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
