from .base import *

DEBUG = False

# TODO: configurar el dominio al hacer deploy a production
# TODO: para pruebas en local agregar 'localhost', '127.0.0.1'
ALLOWED_HOSTS = os.getenv('localhost', '127.0.0.1', 'midominio-production.com').split(',')

# TODO: configurar db para production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'mydatabase'),
        'USER': os.getenv('DB_USER', 'myuser'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'mypassword'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

os.environ['DJANGO_PORT'] = '8080'