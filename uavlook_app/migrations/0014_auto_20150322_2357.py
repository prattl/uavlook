# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0013_slideshow_slideshowimage_slideshowvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', help_text='Include either an image or a video URL, but not both.')),
                ('video_url', models.CharField(verbose_name='URL', max_length=240, help_text='The full URL to a YouTube or Vimeo video page (not embedded URL).')),
                ('order', models.IntegerField()),
                ('slideshow', models.ForeignKey(to='uavlook_app.Slideshow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='slideshowimage',
            name='slideshow',
        ),
        migrations.DeleteModel(
            name='SlideshowImage',
        ),
        migrations.RemoveField(
            model_name='slideshowvideo',
            name='slideshow',
        ),
        migrations.DeleteModel(
            name='SlideshowVideo',
        ),
    ]
