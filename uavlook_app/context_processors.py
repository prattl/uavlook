from .models import MenuSettings


def menu_settings_context_processor(request):
    try:
        settings = MenuSettings.objects.all()[0]
    except:
        settings = None

    return {
        'menu_settings': settings,
    }