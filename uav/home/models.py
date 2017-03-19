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
    title = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)
    # image = ImageChooserBlock(required=False)
    link = blocks.URLBlock(required=True)

    class Meta:
        template = 'home/blocks/header.html'


class HomePage(Page):
    description = RichTextField(blank=True)

    header_images = StreamField([
        ('header_image', ImageChooserBlock(template='home/blocks/header_image.html'))
    ], null=True, help_text='Make sure you have exactly 2 header images for this page.')

    headers = StreamField([
        ('header', HeaderBlock())
    ], null=True, help_text='Make sure you have exactly 3 headers for this page.')

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        StreamFieldPanel('header_images'),
        StreamFieldPanel('headers'),
    ]
