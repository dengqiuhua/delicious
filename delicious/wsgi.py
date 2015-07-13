"""
WSGI config for delicious project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "delicious.settings")

import sys
# website root path
app_path = os.path.dirname(__file__)
workspace = os.path.dirname(app_path)
sys.path.append(workspace)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()