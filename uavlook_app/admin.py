from django.contrib import admin
from uavlook_app.models import Slideshow, SlideshowMedia, InquiryType, \
    ContactForm, ContactFormSubmission, MenuSettings


class ContactFormSubmissionAdmin(admin.ModelAdmin):
    model = ContactFormSubmission
    list_display = ('name', 'email', 'phone', 'inquiry_type', 'created', 'message')
    fields = ('name', 'email', 'phone', 'message', 'inquiry_type', 'contact_form', 'created', )
    readonly_fields = ('created', )

# Register your models here.
admin.site.register(Slideshow)
admin.site.register(SlideshowMedia)
admin.site.register(InquiryType)
admin.site.register(ContactForm)
admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)
admin.site.register(MenuSettings)