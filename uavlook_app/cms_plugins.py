from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext_lazy as _
from djangocms_picture.cms_plugins import PicturePlugin

from uavlook_app.models import BackgroundPicture, ContentSection


class BackgroundPicturePlugin(CMSPluginBase):
    model = BackgroundPicture
    name = _("Background Picture")
    render_template = 'cms/plugins/background_picture.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        header= instance.header
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
        



plugin_pool.register_plugin(BackgroundPicturePlugin)
plugin_pool.register_plugin(ContentSectionPlugin)
plugin_pool.register_plugin(ThreeColumnsPlugin)
