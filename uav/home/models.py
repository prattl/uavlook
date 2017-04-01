from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailcore.fields import (
    RichTextField,
    StreamField,
)
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet


def create_image_field(**kwargs):
    args = {
        'null': True,
        'blank': True,
        'on_delete': models.SET_NULL,
        'related_name': '+',
    }
    args.update(kwargs)
    return models.ForeignKey(
        'wagtailimages.Image',
        **args
    )


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


class AboutPageSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=False)
    content = blocks.RichTextBlock(required=True)

    class Meta:
        template = 'home/blocks/about_page_section.html'


class AboutPage(Page):
    header_image = create_image_field()
    header_text = models.CharField(max_length=128, blank=True, null=True)
    header_description = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True)
    content_sections = StreamField([
        ('sections', AboutPageSectionBlock())
    ], null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('header_text', classname="full"),
        FieldPanel('header_description', classname="full"),
        FieldPanel('description', classname="full"),
        StreamFieldPanel('content_sections'),
    ]

    parent_page_types = ['home.HomePage']


class PhotographyPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label='Gallery Images')
    ]

    parent_page_types = ['home.HomePage']


class PhotographyPageGalleryImage(Orderable):
    page = ParentalKey(PhotographyPage, related_name='gallery_images')
    image = create_image_field(on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=256)
    description = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]


class VideoPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_videos', label='Gallery Videos')
    ]

    parent_page_types = ['home.HomePage']


class VideoPageGalleryVideo(Orderable):
    page = ParentalKey(VideoPage, related_name='gallery_videos')
    video_url = models.URLField(help_text='Full link to a YouTube or Vimeo video page.')
    splash_image = create_image_field(
        help_text='If provided, will be used as the splash image before the video starts.')
    thumbnail_image = create_image_field(
        help_text='If provided, will be used as the thumbnail at the bottom of the video player.')

    panels = [
        FieldPanel('video_url'),
        ImageChooserPanel('splash_image'),
        ImageChooserPanel('thumbnail_image'),
    ]


class ServicesPage(Page):
    header_image = create_image_field()
    header_text = models.CharField(max_length=128, blank=True, null=True)
    header_description = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('header_text', classname="full"),
        FieldPanel('header_description', classname="full"),
        FieldPanel('description', classname="full"),
        InlinePanel('service_sections', label='Service Sections')
    ]

    parent_page_types = ['home.HomePage']


class ServicesPageSection(Orderable):
    page = ParentalKey(ServicesPage, related_name='service_sections')
    title = models.CharField(max_length=128, blank=True, null=True)
    description = RichTextField(blank=True)
    image = create_image_field()
    icon = models.CharField(
        max_length=128, blank=True, null=True,
        help_text="Use the icon name from this list: http://fontawesome.io/icons/ (e.g. 'fa-address-book')"
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
        FieldPanel('icon'),
    ]


class ContactUsPage(AbstractEmailForm):
    header_image = create_image_field()
    header_text = models.CharField(max_length=128, blank=True, null=True)
    description = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('header_text', classname="full"),
        FieldPanel('description', classname="full"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
        InlinePanel('form_fields', label='Form Fields')
    ]

    # def get_form_fields(self):
    #     return self.custom_form_fields.all()


class FormField(AbstractFormField):
    page = ParentalKey(ContactUsPage, related_name='form_fields')


@register_snippet
class SiteFooter(models.Model):
    logo = create_image_field()
    description = models.CharField(max_length=128, blank=True, null=True)
    address_1 = models.CharField(max_length=128, blank=True, null=True)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    address_3 = models.CharField(max_length=128, blank=True, null=True)
    address_4 = models.CharField(max_length=128, blank=True, null=True)

    additional_text_1 = models.CharField(max_length=128, blank=True, null=True)
    additional_text_2 = models.CharField(max_length=128, blank=True, null=True)

    facebook = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
