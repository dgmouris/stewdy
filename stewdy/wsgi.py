"""
WSGI config for stewdy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stewdy.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/dgmouris/mysite/mysite/settings.py'
## and your manage.py is is at '/home/dgmouris/mysite/manage.py'
path = '/home/dgmouris/stewdy'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'stewdy.settings.production'
#
## then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()