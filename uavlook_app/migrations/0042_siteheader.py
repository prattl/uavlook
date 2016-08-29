# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
        ('uavlook_app', '0041_auto_20150430_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, to='cms.CMSPlugin', serialize=False, parent_link=True)),
                ('title', models.CharField(verbose_name='title', blank=True, max_length=240, null=True)),
                ('logo', models.ImageField(verbose_name='Logo Image', blank=True, null=True, upload_to=cms.models.pluginmodel.get_plugin_media_path)),
                ('logo_width', models.IntegerField(verbose_name='Logo Width', default='500', help_text='Width of the logo image measured in px. The height will automatically scale with the width.')),
                ('image', models.ImageField(verbose_name='image', upload_to=cms.models.pluginmodel.get_plugin_media_path)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, default=10.0, help_text='The height of this image measured in rem. 1 rem is about 16px.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
