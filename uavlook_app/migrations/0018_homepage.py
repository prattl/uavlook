# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0017_remove_threecolumns_horizontal'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='cms.CMSPlugin')),
                ('title', models.CharField(verbose_name='title', blank=True, null=True, max_length=240)),
                ('header', models.CharField(verbose_name='header', blank=True, null=True, max_length=240)),
                ('subheader', models.CharField(verbose_name='sub header', blank=True, null=True, max_length=240)),
                ('opacity', models.DecimalField(help_text="The opacity of this page's background. 0.00 is transparent, and 1.00 is all black. Use up to 2 decimal places.", decimal_places=2, default=0.0, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
