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
    top = models.BooleanField(default=False, help_text='Check if this image should appear at the top of the page.')
    shade_amount = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, help_text='The amount of shading to add to the image. 0.00 is no shading, and 1.00 is all black. Use up to 2 decimal places.')


class ContentSection(CMSPlugin):
    title = models.CharField(_('title'), max_length=240)
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)
    center = models.BooleanField(_('center'), default=False, help_text='Check if the contents of this section should be centered. If not, they will be left-justified.')

    def __unicode__(self):
        return unicode(self.title)


