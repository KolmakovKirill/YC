import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'dev-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Настройки Yandex Object Storage
AWS_STORAGE_BUCKET_NAME = 'todo-static-89cloud'
AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
AWS_ACCESS_KEY_ID = 'ajes81nqmuomi43o6qvi'
AWS_SECRET_ACCESS_KEY = 'MIEvQIBADANBgkqhkiG9w0BAQEFAASCBSkwggSBAgEAAoIBAQDTql4CfxQWr2TXkVZpyw8WKURjwAm/KbyO/qjymKFkbnUKeKdbQFtFsdG+hRidaMR15nhowWGbU7T2T2uNi4Au7paSKSObjIrrVKR9c7HYkdVRhi9vSkf9bY1L9OVkjcPRkbBq43VgOAcRVD'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = f'https://storage.yandexcloud.net/{AWS_STORAGE_BUCKET_NAME}/'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'notes',
]

ROOT_URLCONF = 'todo.urls'

MIDDLEWARE = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo',
        'USER': 'todo_user',
        'PASSWORD': 'TodoApp123!',
        'HOST': 'rc1a-2or8kebmje6lvohe.mdb.yandexcloud.net',
        'PORT': '6432',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'app/notes/static')]
