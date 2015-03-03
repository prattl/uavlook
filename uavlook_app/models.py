from django.db import models
import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path on django CMS 3.0.4+ for information
        """
        return instance.get_media_path(filename)


class BackgroundPicture(CMSPlugin):
    image = models.ImageField(_("image"), upload_to=get_plugin_media_path)
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)
    subheader = models.CharField(_('subheader'), max_length=240, null=True, blank=True)

