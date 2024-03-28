"""
WSGI config for config project.

It exposes the WSGi callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the sys.path
project_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(project_dir)
sys.path.insert(0, project_root)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Import and instantiate the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
