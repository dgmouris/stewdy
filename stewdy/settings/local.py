#this is going to be the local settings.

#if there are erros you can do this.
#export PYTHONPATH=$PYTHONPATH:$PWD
from .base import *
DEBUG = True
ALLOWED_HOSTS += 'localhost'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

