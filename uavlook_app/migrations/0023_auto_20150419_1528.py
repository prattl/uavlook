# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uavlook_app', '0022_auto_20150419_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='data_fit',
            field=models.CharField(verbose_name='Data Fit', help_text='How the images should fit inside the slideshow. See http://fotorama.io/customize/fit/ for more informatioon,', max_length=240, default='cover', choices=[('contain', 'Contain'), ('cover', 'Cover'), ('scaledown', 'Scale Down'), ('none', 'None')]),
            preserve_default=True,
        ),
    ]
