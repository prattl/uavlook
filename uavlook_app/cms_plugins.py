from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext_lazy as _
from djangocms_picture.cms_plugins import PicturePlugin

from uavlook_app.models import BackgroundPicture




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


plugin_pool.register_plugin(BackgroundPicturePlugin)
