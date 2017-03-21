from django import template
from home.models import SiteFooter

register = template.Library()


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def site_footer(context):
    return {
        'footer': SiteFooter.objects.first(),
        'request': context['request'],
    }
