from .base import *

ALLOWED_HOSTS = ['3.35.191.255']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASEs = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'g6=cbzwNeooAMk+nR:5jD&9W&`qCf?3#',
        'HOST': 'ls-83e0d565962a60e921f1654524ab43fc552c14bd.chnosgxs5ver.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}