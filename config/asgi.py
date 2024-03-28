"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Get the ASGI application
application = get_asgi_application()

# If the ASGI_SERVER environment variable is set to Daphne, wrap the application
# in Daphne's ASGI handler
if os.environ.get("ASGI_SERVER") == "Daphne":
    from daphne.www.application import WSGIApplication

    application = WSGIApplication(application)
