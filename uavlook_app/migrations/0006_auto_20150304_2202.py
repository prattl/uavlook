# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0005_backgroundpicture_shade_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeColumns',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=240, null=True, blank=True, verbose_name='title')),
                ('header', models.CharField(max_length=240, null=True, blank=True, verbose_name='header')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='backgroundpicture',
            name='title',
            field=models.CharField(max_length=240, null=True, blank=True, verbose_name='title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contentsection',
            name='title',
            field=models.CharField(max_length=240, null=True, blank=True, verbose_name='title'),
            preserve_default=True,
        ),
    ]
