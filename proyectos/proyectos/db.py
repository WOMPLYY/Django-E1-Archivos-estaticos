import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huertadbpy',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}