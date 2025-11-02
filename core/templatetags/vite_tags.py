from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
import os
import json

register = template.Library()

@register.simple_tag(takes_context=True)
def vite_hmr_client(context):
    """
    Template tag to include the Vite HMR client. Only used in development.
    """
    if not settings.DEBUG:
        return ''
    
    return mark_safe(
        f'<script type="module" src="{settings.VITE_DEV_SERVER_URL}/@vite/client"></script>'
    )

@register.simple_tag(takes_context=True)
def vite_asset(context, path):
    """
    Template tag to include Vite assets. In development, it will use the Vite dev server.
    In production, it will use the hashed file names from the manifest.
    """
    if settings.DEBUG:
        # In development, load from Vite dev server
        return f'{settings.VITE_DEV_SERVER_URL}/src/{path}'
    
    # In production, load from manifest
    manifest_path = os.path.join(settings.BASE_DIR, 'dist', 'manifest.json')
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        if path in manifest:
            return f'/static/{manifest[path]["file"]}'
        
        # If the path is not found, try with leading slash
        if f'/{path}' in manifest:
            return f'/static/{manifest[f"/{path}"]["file"]}'
        
        # If still not found, return the original path
        return f'/static/{path}'
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        if settings.DEBUG:
            print(f'Vite manifest not found or invalid: {e}')
        return f'/static/{path}'

@register.inclusion_tag('vite_assets.html', takes_context=True)
def vite_assets(context):
    """
    Template tag to include all Vite assets (CSS and JS) based on the manifest.
    """
    if settings.DEBUG:
        # In development, we only need to include the main entry point
        # The rest will be handled by Vite's HMR
        return {
            'is_development': True,
            'vite_hmr_url': f'{settings.VITE_DEV_SERVER_URL}/src/main.js',
        }
    
    # In production, include all assets from the manifest
    manifest_path = os.path.join(settings.BASE_DIR, 'dist', 'manifest.json')
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Find the main entry point
        main_entry = next((v for v in manifest.values() if 'isEntry' in v), None)
        
        if not main_entry:
            return {'is_development': False, 'css_files': [], 'js_files': []}
        
        # Get all CSS and JS files
        css_files = [f'/static/{f}' for f in main_entry.get('css', [])]
        js_files = [f'/static/{main_entry["file"]}']
        
        # Add dynamic imports if any
        if 'dynamicImports' in main_entry:
            for dep in main_entry['dynamicImports']:
                if dep in manifest and 'file' in manifest[dep]:
                    js_files.append(f'/static/{manifest[dep]["file"]}')
        
        return {
            'is_development': False,
            'css_files': css_files,
            'js_files': js_files,
        }
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        if settings.DEBUG:
            print(f'Vite manifest not found or invalid: {e}')
        return {'is_development': False, 'css_files': [], 'js_files': []}
