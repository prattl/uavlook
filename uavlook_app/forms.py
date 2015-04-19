from django.forms import ModelForm, Textarea

from uavlook_app.models import ContactFormSubmission


class ContactFormSubmissionForm(ModelForm):
    class Meta:
        model = ContactFormSubmission
        field = '__all__'
        widgets = {
            'message': Textarea(attrs={'cols': 80, 'rows': 8}),
        }