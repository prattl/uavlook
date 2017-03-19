# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 02:24
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170318_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='additional_description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='additional_header',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='content_sections',
            field=wagtail.wagtailcore.fields.StreamField((('sections', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))),), null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='header',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='header_images',
            field=wagtail.wagtailcore.fields.StreamField((('header_image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='home/blocks/header_image.html')),), help_text='Make sure you have exactly 2 header images for this page.', null=True),
        ),
    ]