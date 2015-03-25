# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('uavlook_app', '0012_contactform_contactformsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', parent_link=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=240, blank=True, verbose_name='title', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlideshowImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('order', models.IntegerField()),
                ('slideshow', models.ForeignKey(to='uavlook_app.Slideshow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlideshowVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.CharField(max_length=240, help_text='The full URL to a YouTube or Vimeo video page (not embedded URL).', verbose_name='URL')),
                ('order', models.IntegerField()),
                ('slideshow', models.ForeignKey(to='uavlook_app.Slideshow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
