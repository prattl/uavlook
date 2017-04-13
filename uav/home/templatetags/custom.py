from django import template

register = template.Library()


@register.filter
def get_key_value(some_dict, key):
    return some_dict.get(key, '')


@register.filter
def get_form_field(form, key):
    return getattr(form, key, '')

