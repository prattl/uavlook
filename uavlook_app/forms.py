from django.forms import ModelForm, Textarea
from django.forms import Widget

from uavlook_app.models import ContactFormSubmission

old_build_attrs = Widget.build_attrs


def build_attrs(self, extra_attrs=None, **kwargs):
    attrs = old_build_attrs(self, extra_attrs, **kwargs)

    if self.is_required:
        attrs["required"] = "required"

    return attrs

Widget.build_attrs = build_attrs


class ContactFormSubmissionForm(ModelForm):
    class Meta:
        model = ContactFormSubmission
        # exclude = ['contact_form']
        fields = '__all__'
        widgets = {
            'message': Textarea(attrs={'cols': 80, 'rows': 5, 'required': 'required'}),
        }

    def save(self, commit=True):
        print('Form save.')
        return super(ContactFormSubmissionForm, self).save(commit)