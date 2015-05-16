from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.contrib import admin
from djangocms_text_ckeditor.models import Text
from djangocms_text_ckeditor.cms_plugins import TextPlugin
from django.utils.translation import ugettext_lazy as _

from uavlook_app.models import BackgroundPicture, ContentSection, ThreeColumns, \
    SiteHeader, SocialMedia, BlockQuote, ContactForm, Slideshow, SlideshowMedia, HomePage
from uavlook_app.forms import ContactFormSubmissionForm


class BackgroundPicturePlugin(CMSPluginBase):
    model = BackgroundPicture
    name = _("Background Picture")
    render_template = 'cms/plugins/background_picture.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        # header = instance.header
        subheader = instance.subheader
        context.update({
            'picture': instance,
            # 'header': header,
            'subheader': subheader,
            'height': instance.height,
            'logo': instance.header_logo,
            'logo_width': instance.logo_width,
        })
        return context


class ContentSectionPlugin(CMSPluginBase):
    model = ContentSection
    name = _('Content Section')
    render_template = 'cms/plugins/content_section.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        header = instance.header
        context.update({
            'header': header,
            'instance': instance,
        })
        return context


class ThreeColumnsPlugin(CMSPluginBase):
    model = ThreeColumns
    name = _('Three Columns')
    render_template = 'cms/plugins/three_columns.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        children = instance.child_plugin_instances
        context.update({
            'instance': instance,
        })
        return context


class ContainerPlugin(CMSPluginBase):
    name = _('Container')
    render_template = 'cms/plugins/container.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context
        

class FooterPlugin(CMSPluginBase):
    name = _('Footer')
    render_template = 'cms/plugins/footer.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        children = instance.child_plugin_instances
        context.update({
            'instance': instance,
        })
        return context


class SiteHeaderPlugin(CMSPluginBase):
    model = SiteHeader
    name = _('Header')
    render_template = 'cms/plugins/site_header.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        for plugin in instance.child_plugin_instances:
            if type(plugin) is Text:
                context.update({'text_plugin': plugin})
        context.update({
            'instance': instance,
        })
        return context


class SocialMediaPlugin(CMSPluginBase):
    model = SocialMedia
    name = _('Social Media')
    render_template = 'cms/plugins/social_media.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class BlockQuotePlugin(CMSPluginBase):
    model = BlockQuote
    name = _('Block Quote')
    render_template = 'cms/plugins/block_quote.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ContactFormPlugin(CMSPluginBase):
    model = ContactForm
    name = _('Contact Form')
    render_template = 'cms/plugins/contact_form.html'

    def render(self, context, instance, placeholder):
        form = ContactFormSubmissionForm(initial={'contact_form': instance})
        context.update({
            'instance': instance,
            'contact_form': form,
        })
        return context


class SlideshowMediaInlineAdmin(admin.StackedInline):
    model = SlideshowMedia


class SlideshowPlugin(CMSPluginBase):
    model = Slideshow
    name = _('Slideshow')
    render_template = 'cms/plugins/slideshow.html'
    inlines = (SlideshowMediaInlineAdmin,)

    def render(self, context, instance, placeholder):
        media = instance.slideshowmedia_set.all()
        context.update({
            'instance': instance,
            'media': media,
        })
        return context


class HomePagePlugin(CMSPluginBase):
    model = HomePage
    name = _('Home Page')
    render_template = 'cms/plugins/homepage.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        for plugin in instance.child_plugin_instances:
            # import pdb; pdb.set_trace()
            if type(plugin) is Slideshow:
                context.update({'slideshow': plugin})
            if type(plugin) is SocialMedia:
                context.update({'social_media': plugin})
            if type(plugin) is Text:
                context.update({'text_plugin': plugin})
        context.update({
            'instance': instance,
            'homepage': True,
        })
        return context


plugin_pool.register_plugin(BackgroundPicturePlugin)
plugin_pool.register_plugin(ContentSectionPlugin)
plugin_pool.register_plugin(ThreeColumnsPlugin)
plugin_pool.register_plugin(FooterPlugin)
plugin_pool.register_plugin(SiteHeaderPlugin)
plugin_pool.register_plugin(SocialMediaPlugin)
plugin_pool.register_plugin(BlockQuotePlugin)
plugin_pool.register_plugin(ContactFormPlugin)
plugin_pool.register_plugin(SlideshowPlugin)
plugin_pool.register_plugin(HomePagePlugin)
