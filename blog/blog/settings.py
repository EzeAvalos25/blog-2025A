import os
from dotenv import load_dotenv

load_dotenv(encoding='utf-8')

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

if DJANGO_ENV == 'production':
    from .configurations.production import *
else:
    from .configurations.local import *