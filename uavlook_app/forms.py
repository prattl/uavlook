from django.forms import ModelForm

from uavlook_app.models import ContactFormSubmission


class ContactFormSubmissionForm(ModelForm):
    class Meta:
        model = ContactFormSubmission
        field = '__all__'