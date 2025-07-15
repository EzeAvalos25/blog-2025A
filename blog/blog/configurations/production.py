from .base import *

DEBUG = False
cl
# TODO: configurar el dominio al hacer deploy a production
ALLOWED_HOSTS = ["midominio-production.com"]

# TODO: configurar db para production
DATABASES = {
    'default': {
          'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        # en caso de usar postgresql o mysql, descomentar la línea correspondiente
          
        #'ENGINE': 'django.db.backends.postgresql',
        #'ENGINE': 'django.db.backends.mysql',

        #'NAME': os.getenv('DB_NAME'),

        #'USER': os.getenv('DB_USER'),

        #'PASSWORD': os.getenv('DB_PASSWORD'),

        #'HOST': os.getenv('DB_HOST'),

        #'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = '8080'