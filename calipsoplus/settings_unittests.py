from calipsoplus.settings import *

ALLOWED_HOSTS = []

DJANGO_ENV = 'LOCAL'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    },
    'guacamole': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'guacamole'
    }
}

# logs
LOGGING['loggers']['apprest']['handlers'] = ['console']

TESTING_MODE = True

# docker location
DOCKER_URL_DAEMON = "tcp://192.168.33.13:2375"
REMOTE_MACHINE_IP = "192.168.33.13"
