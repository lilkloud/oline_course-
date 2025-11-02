from django.conf import settings

def vite_assets(request):
    """
    Add Vite assets to the template context.
    """
    is_production = not settings.DEBUG
    return {
        'is_production': is_production,
        'vite_dev_server_url': settings.VITE_DEV_SERVER_URL,
        'vite_assets_path': '/static/assets/' if is_production else ''
    }
