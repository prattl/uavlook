# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0011_auto_20150308_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', parent_link=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=240, verbose_name='title', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.CharField(max_length=240, verbose_name='Email')),
                ('phone', models.CharField(max_length=240, verbose_name='Phone Number', blank=True, null=True)),
                ('message', models.CharField(max_length=2400, verbose_name='Message', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
