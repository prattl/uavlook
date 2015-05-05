# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0042_siteheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('menu_font_color', models.CharField(verbose_name='Menu Font Color', help_text='Enter a 6 digit color hex code.', max_length=6, default='FFFFFF')),
                ('menu_font_weight', models.CharField(verbose_name='Menu Font Weight', choices=[('normal', 'Normal'), ('bold', 'Bold')], max_length=24, default='normal')),
                ('menu_font_size', models.CharField(verbose_name='Menu Font Size', help_text='Specify a font size in rem units. 1 rem is normal text size.', max_length=2, default='1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
