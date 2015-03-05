# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0007_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', parent_link=True, serialize=False, auto_created=True)),
                ('title', models.CharField(null=True, max_length=240, blank=True, verbose_name='title')),
                ('facebook', models.CharField(null=True, max_length=240, blank=True, verbose_name='Facebook')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
