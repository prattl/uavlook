from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page

import threading


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
    height = models.DecimalField(default=10.00, max_digits=5, decimal_places=2,
                                 help_text='The height of this image measured in rem. 1 rem is about 16px.')
    header_logo = models.ImageField(_("Logo Image"), null=True, blank=True, upload_to=get_plugin_media_path)
    logo_width = models.IntegerField('Logo Width',
                                     default='500', help_text='Width of the logo image measured in px. The height will automatically scale with the width.')


class ContentSection(UAVPlugin):
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)
    center = models.BooleanField(_('center'), default=False,
                                 help_text='Check if the contents of this section should be centered. If not, they will be left-justified.')
    # opacity = models.DecimalField(default=0.00, max_digits=3, decimal_places=2,
    #                                 help_text='The opacity of this section\'s background. 0.00 is transparent, and 1.00 is all black. Use up to 2 decimal places.')


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
    recipients = models.ManyToManyField(User, help_text='Recipients to send contact emails to.')

    def recipients_list(self):
        return [user.email for user in self.recipients.all()]

    def __str__(self):
        return 'Contact form for recipients: %s' % [rec.email for rec in self.recipients.all()]


class InquiryType(models.Model):
    type = models.CharField(_('Type'), max_length=240)

    def __str__(self):
        return self.type


class ContactFormSubmission(models.Model):
    name = models.CharField(_('Name'), max_length=240)
    email = models.CharField(_('Email'), max_length=240)
    phone = models.CharField(_('Phone Number'), max_length=240, default='')
    message = models.CharField(_('Message'), max_length=2400, null=True, blank=True)
    inquiry_type = models.ForeignKey(InquiryType)
    contact_form = models.ForeignKey(ContactForm)\

    def __str__(self):
        return 'Contact Submission from {} at {}'.format(self.name, self.email)

    def save(self, *args, **kwargs):
        print('Contact form submission save.')
        print('Sending email to: ', self.contact_form.recipients.all())
        print('Starting email thread.')
        email_thread = threading.Thread(target=send_email_thread,
                                        args=(self,))
        email_thread.start()
        print('Email thread started.')
        super(ContactFormSubmission, self).save(*args, **kwargs)


def send_email_thread(form_submission):
    recipients = form_submission.contact_form.recipients_list()
    # sender = 'support@uavlook.com'
    sender = 'Lenny@prattdev.net'
    subject = 'New Inquiry from uavlook.com'
    message = """
    Somebody submitted a Contact form on uavlook.com with the following information:

    Name: {}
    Email: {}
    Phone: {}
    Inquiry Type: {}
    Message: {}

    """.format(form_submission.name, form_submission.email, form_submission.phone,
               form_submission.inquiry_type, form_submission.message)
    send_mail(subject=subject, message=message, from_email=sender, recipient_list=recipients, fail_silently=False)


class Slideshow(UAVPlugin):
    ARROW_CHOICES = [
        ('always', 'Always display arrows'),
        ('true', 'Display arrows on hover'),
        ('false', 'Never display arrows'),
    ]

    DATA_FIT_CHOICES = [
        ('contain', 'Contain'),
        ('cover', 'Cover'),
        ('scaledown', 'Scale Down'),
        ('none', 'None'),
    ]

    DATA_TRANSITION_CHOICES = [
        ('slide', 'Slide'),
        ('crossfade', 'Crossfade (dissolve)'),
    ]

    show_thumbnails = models.BooleanField(_('Show Thumbnails'), default=True, help_text='Check to display thmbnails below the slideshow.')
    show_arrows = models.CharField(_('Navigation Arrows'), default='true', help_text='Navigation Arrows',
                                   choices=ARROW_CHOICES, max_length=240)
    data_click = models.BooleanField(_('Data Click'), default=True, help_text='Check to enable users to click anywhere on the slideshow to advance to the next or previous image. Default is True.')
    data_swipe = models.BooleanField(_('Data Swipe'), default=True, help_text='Check to enable users to swipe on the slideshow to advance to the next or previous image. Default is True.')
    data_fit = models.CharField(_('Data Fit'), default='cover',
                                help_text='How the images should fit inside the slideshow. See http://fotorama.io/customize/fit/ for more informatioon,',
                                choices=DATA_FIT_CHOICES, max_length=240)
    data_transition = models.CharField(_('Data Transition'), null=True, blank=True, max_length=56,
                                       help_text='Type of transition. Default is slide.',
                                       choices=DATA_TRANSITION_CHOICES)
    data_shuffle = models.BooleanField(_('Data Shuffle'), default=False,
                                       help_text='Check to shuffle the images in a random order when the page loads.')
    data_width = models.CharField(_('Data Width'), null=True, blank=True, max_length=5,
                                  help_text='Width of the slideshow. Specify a whole number (600) or a percent (100%).')
    data_height = models.CharField(_('Data Height'), null=True, blank=True, max_length=5,
                                  help_text='Height of the slideshow. Specify a whole number (600) or a percent (100%).')
    data_ratio = models.CharField(_('Data Ratio'), null=True, blank=True, max_length=24,
                                  help_text='Aspect Ratio of the slideshow. Specify either a decimal (1.333) or a fraction (800/600 or 4/3).')
    data_loop = models.BooleanField(_('Data Loop'), default=False, help_text='Check this to loop to the beginning of the slideshow when the end is reached.')
    data_autoplay = models.IntegerField(_('Data Autoplay'), null=True, blank=True,
                                        help_text='Enter a number here to enable auto-play. Enter the number of milliseconds to specify how long each image should appear. For example, for 5 seconds enter 5000.')
    data_stopautoplayontouch = models.BooleanField(_('Data Stop Autoplay On Touch'), default=True,
                                                   help_text='Uncheck this to enable autoplay on touch devices (if a number was entered above). By default, autoplay is not enabled on touch devices.')
    data_transitionduration = models.IntegerField(_('Data Transition Duration'), null=True, blank=True,
                                                  help_text='Enter a number to control the duration of the transition effect in milliseconds. For example to fade to the next image in 0.5 seconds, enter 500.')

    def copy_relations(self, oldinstance):
        print('Running copy_relations')
        for associated_item in oldinstance.slideshowmedia_set.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.slideshow = self
            associated_item.save()


class SlideshowMedia(models.Model):
    image = models.ImageField(null=True, blank=True, help_text='Include either an image or a video URL, but not both.')
    video_url = models.CharField(_('URL'), max_length=240, null=True, blank=True, help_text='The full URL to a YouTube or Vimeo video page (not embedded URL).')
    slideshow = models.ForeignKey(Slideshow)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']


class HomePage(UAVPlugin):
    FONT_WEIGHT_CHOICES = [
        ('normal', 'Normal'),
        ('bold', 'Bold'),
    ]
    header = models.CharField(_('header'), max_length=240, null=True, blank=True)
    subheader = models.CharField(_('sub header'), max_length=240, null=True, blank=True)
    opacity = models.DecimalField(default=0.00, max_digits=3, decimal_places=2,
                                    help_text='The opacity of this page\'s background. 0.00 is transparent, and 1.00 is all black. Use up to 2 decimal places.')
    logo = models.ImageField(_("Logo Image"), null=True, blank=True, upload_to=get_plugin_media_path)
    logo_width = models.IntegerField('Logo Width',
                                     default='500', help_text='Width of the logo image measured in px. The height will automatically scale with the width.')
    # header_fontsize = models.CharField(_('Header Font Size'), max_length=12, null=True, blank=True,
    #                                    help_text='Use a decimal, 1 is normal text and 2 is double that size, etc.')
    # header_fontweight = models.CharFIeld('Header Font Weight', choices=FONT_WEIGHT_CHOICES)


# class SiteHeader(UAVPlugin):
#     logo = models.ImageField(_("Logo Image"), null=True, blank=True, upload_to=get_plugin_media_path)
#     background_image =