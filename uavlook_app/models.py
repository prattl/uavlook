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


class UAVPlugin(CMSPlugin):
    """
    Abstract plugin that adds a title field.
    """
    title = models.CharField(_('title'), max_length=240, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.title)


class BackgroundPicture(UAVPlugin):
    image = models.ImageField(_("image"), upload_to=get_plugin_media_path)
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)
    subheader = models.CharField(_('subheader'), max_length=240, null=True, blank=True)
    top = models.BooleanField(default=False, help_text='Check if this image should appear at the top of the page.')
    shade_amount = models.DecimalField(default=0.00, max_digits=3, decimal_places=2,
                                       help_text='The amount of shading to add to the image. 0.00 is no shading, and 1.00 is all black. Use up to 2 decimal places.')


class ContentSection(UAVPlugin):
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)
    center = models.BooleanField(_('center'), default=False,
                                 help_text='Check if the contents of this section should be centered. If not, they will be left-justified.')


class ThreeColumns(UAVPlugin):
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)


class Footer(UAVPlugin):
    pass


class SocialMedia(UAVPlugin):
    facebook = models.CharField(_('Facebook URL'), max_length=240, null=True, blank=True)
    google_plus = models.CharField(_('Google Plus URL'), max_length=240, null=True, blank=True)
    instagram = models.CharField(_('Instagram URL'), max_length=240, null=True, blank=True)
    twitter = models.CharField(_('Twitter URL'), max_length=240, null=True, blank=True)
    youtube = models.CharField(_('Youtube URL'), max_length=240, null=True, blank=True)


class BlockQuote(UAVPlugin):
    quote = models.TextField(_('Quote'))
    attribution = models.CharField(_('Attribution'), max_length=240, null=True, blank=True)


class ContactForm(UAVPlugin):
    pass


class ContactFormSubmission(models.Model):
    name = models.CharField(_('Name'), max_length=240)
    email = models.CharField(_('Email'), max_length=240)
    phone = models.CharField(_('Phone Number'), max_length=240, null=True, blank=True)
    message = models.CharField(_('Message'), max_length=2400, null=True, blank=True)

    def save(self, *args, **kwargs):
        # TODO: Send email to staff
        super(ContactFormSubmission, self).save(*args, **kwargs)
