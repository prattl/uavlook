from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext_lazy as _

from uavlook_app.models import BackgroundPicture, ContentSection, ThreeColumns, Footer, SocialMedia, BlockQuote, ContactForm
from uavlook_app.forms import ContactFormSubmissionForm


class BackgroundPicturePlugin(CMSPluginBase):
    model = BackgroundPicture
    name = _("Background Picture")
    render_template = 'cms/plugins/background_picture.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        header = instance.header
        subheader = instance.subheader
        context.update({
            'picture': instance,
            'header': header,
            'subheader': subheader
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
        print("Number of children in 3 cols: %s" % len(children))
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
        print("Number of children in footer: %s" % len(children))
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
    name = _('Contact Form')
    render_template = 'cms/plugins/contact_form.html'

    def render(self, context, instance, placeholder):
        form = ContactFormSubmissionForm()
        context.update({
            'instance': instance,
            'contact_form': form,
        })
        return context


plugin_pool.register_plugin(BackgroundPicturePlugin)
plugin_pool.register_plugin(ContentSectionPlugin)
plugin_pool.register_plugin(ThreeColumnsPlugin)
plugin_pool.register_plugin(FooterPlugin)
plugin_pool.register_plugin(SocialMediaPlugin)
plugin_pool.register_plugin(BlockQuotePlugin)
plugin_pool.register_plugin(ContactFormPlugin)
