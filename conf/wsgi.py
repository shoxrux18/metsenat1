"""
WSGI config for conf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
>>>>>>> b4f84d110abac91e3e728c058c03343c18dccad5
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

application = get_wsgi_application()
