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
    link = blocks.URLBlock(required=True)

    class Meta:
        template = 'home/blocks/header.html'


class HomePageSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = 'home/blocks/home_page_section.html'


class HomePage(Page):
    header_images = StreamField([
        ('header_image', ImageChooserBlock(template='home/blocks/header_image.html'))
    ], null=True, help_text='Make sure you have exactly 2 header images for this page.')
    headers = StreamField([
        ('header', HeaderBlock())
    ], null=True, help_text='Make sure you have exactly 3 headers for this page.')
    description = RichTextField(blank=True)
    header = models.CharField(max_length=128, blank=True, null=True)
    content_sections = StreamField([
        ('sections', HomePageSectionBlock())
    ], null=True)
    additional_header = RichTextField(blank=True, null=True)
    additional_description = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('header_images'),
        StreamFieldPanel('headers'),
        FieldPanel('description', classname="full"),
        FieldPanel('header', classname="full"),
        StreamFieldPanel('content_sections'),
        FieldPanel('additional_header', classname="full"),
        FieldPanel('additional_description', classname="full"),
    ]
