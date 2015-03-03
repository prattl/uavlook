# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundPicture',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', serialize=False, parent_link=True, auto_created=True, primary_key=True)),
                ('image', models.ImageField(verbose_name='image', upload_to=cms.models.pluginmodel.get_plugin_media_path)),
                ('header', models.CharField(verbose_name='header', null=True, blank=True, max_length=240)),
                ('subheader', models.CharField(verbose_name='subheader', null=True, blank=True, max_length=240)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
