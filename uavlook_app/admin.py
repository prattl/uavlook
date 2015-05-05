from django.contrib import admin
from uavlook_app.models import Slideshow, SlideshowMedia, InquiryType, \
    ContactForm, ContactFormSubmission, MenuSettings

# Register your models here.
admin.site.register(Slideshow)
admin.site.register(SlideshowMedia)
admin.site.register(InquiryType)
admin.site.register(ContactForm)
admin.site.register(ContactFormSubmission)
admin.site.register(MenuSettings)