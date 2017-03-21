# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_sitefooter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitefooter',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
