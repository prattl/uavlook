# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170319_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='header',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
