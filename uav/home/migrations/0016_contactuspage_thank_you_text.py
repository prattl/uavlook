# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 20:38
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_contactuspage_formfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactuspage',
            name='thank_you_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
