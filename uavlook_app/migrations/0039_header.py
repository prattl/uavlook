# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0038_auto_20150430_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('title', models.CharField(blank=True, verbose_name='title', max_length=240, null=True)),
                ('logo', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, blank=True, verbose_name='Logo Image', null=True)),
                ('logo_width', models.IntegerField(default='500', verbose_name='Logo Width', help_text='Width of the logo image measured in px. The height will automatically scale with the width.')),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='image')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, default=10.0, help_text='The height of this image measured in rem. 1 rem is about 16px.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
