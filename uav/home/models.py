from django.db import models

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import (
    RichTextField,
    StreamField,
)
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HeaderBlock(blocks.StructBlock):
    # title = models.CharField('Title', max_length=128, null=True)
    # description = models.CharField('Description', max_length=128, null=True)
    title = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)


class HomePage(Page):
    # heading_1_title = models.CharField('Left Heading Title', max_length=128, null=True)
    # heading_2_title = models.CharField('Center Heading Title', max_length=128, null=True)
    # heading_3_title = models.CharField('Right Heading Title', max_length=128, null=True)
    # heading_1_description = models.CharField('Left Heading Description', max_length=128, null=True)
    # heading_2_description = models.CharField('Center Heading Description', max_length=128, null=True)
    # heading_3_description = models.CharField('Right Heading Description', max_length=128, null=True)
    description = RichTextField(blank=True)

    headers = StreamField([
        # ('heading', blocks.CharBlock(classname="full title")),
        # ('paragraph', blocks.RichTextBlock()),
        # ('image', ImageChooserBlock()),
        ('header', HeaderBlock())
    ], null=True, help_text='Make sure you have exactly 3 headers for this page.')

    content_panels = Page.content_panels + [
        # FieldRowPanel([
        #     FieldPanel('heading_1_title'),
        #     FieldPanel('heading_2_title'),
        #     FieldPanel('heading_3_title'),
        # ]),
        # FieldRowPanel([
        #     FieldPanel('heading_1_description'),
        #     FieldPanel('heading_2_description'),
        #     FieldPanel('heading_3_description'),
        # ]),
        FieldPanel('description', classname="full"),
        StreamFieldPanel('headers'),
    ]
