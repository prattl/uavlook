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


class HomePage(Page):
    heading_1_title = models.CharField('Left Heading Title', max_length=128, null=True)
    heading_2_title = models.CharField('Center Heading Title', max_length=128, null=True)
    heading_3_title = models.CharField('Right Heading Title', max_length=128, null=True)
    description = RichTextField(blank=True)

    # body = StreamField([
    #     ('heading', blocks.CharBlock(classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ], null=True)

    content_panels = Page.content_panels + [
        FieldRowPanel([
            FieldPanel('heading_1_title'),
            FieldPanel('heading_2_title'),
            FieldPanel('heading_3_title'),
        ]),
        FieldPanel('description', classname="full"),
        # StreamFieldPanel('body'),
    ]
