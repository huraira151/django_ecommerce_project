from pathlib import Path
import os
import logging
import environ

env = environ.Env()
env.read_env(".env")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)20irqw=!k8a)&qls^*lt0vieg5&n#a06n^99ck40r(-%7u0(i'

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Social Login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin',
]
LOCAL_APPS = [
    "users",
    "stores",
    "payments",
    "social_login",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "phonenumber_field",
    "phonenumbers",
    "drf_yasg",
    "djstripe",
    "rest_auth",
    "corsheaders",
    "dj_rest_auth",
]

AUTH_USER_MODEL = "users.User"

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://13.50.25.74:8000",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

ROOT_URLCONF = 'ecommerce_project_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web_build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce_project_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if env.str("DATABASE_URL", default=None):
    DATABASES = {"default": env.db(engine='django.contrib.gis.db.backends.postgis')}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'ecommerce_project_django/static'),
                    os.path.join(BASE_DIR, 'web_build/static')]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# AWS S3 config
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", "")
AWS_STORAGE_REGION = env.str("AWS_STORAGE_REGION", "")

USE_S3 = (
        AWS_ACCESS_KEY_ID
        and AWS_SECRET_ACCESS_KEY
        and AWS_STORAGE_BUCKET_NAME
        and AWS_STORAGE_REGION
)

if USE_S3:
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", "public-read")
    AWS_MEDIA_LOCATION = env.str("AWS_MEDIA_LOCATION", "media")
    AWS_AUTO_CREATE_BUCKET = env.bool("AWS_AUTO_CREATE_BUCKET", True)
    DEFAULT_FILE_STORAGE = env.str(
        "DEFAULT_FILE_STORAGE", "home.storage_backends.MediaStorage"
    )
    # MEDIA_URL = "/mediafiles/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# ____________
# Social Login
# ____________
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 1

# This setting is for using email as Username field for allauth ----start----
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MANAGER = 'users.managers.UserManager'
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_ENABLED = True
ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.MySocialAccountAdapter"
ACCOUNT_ALLOW_REGISTRATION = env.bool("ACCOUNT_ALLOW_REGISTRATION", True)
SOCIALACCOUNT_ALLOW_REGISTRATION = env.bool("SOCIALACCOUNT_ALLOW_REGISTRATION", True)
# This setting is for using email as Username field for allauth ----end----

# # >>> Facebook Keys
# SOCIAL_AUTH_FACEBOOK_KEY = env.str("SOCIAL_AUTH_FACEBOOK_KEY")
# SOCIAL_AUTH_FACEBOOK_SECRET = env.str("SOCIAL_AUTH_FACEBOOK_SECRET")

# if you succeed in login, you'll be redirected to the main page.
LOGIN_REDIRECT_URL = "/"

SOCIALACCOUNT_PROVIDERS = {
    'facebook':
        {'METHOD': 'oauth2',
         'SCOPE': ['email', 'public_profile', 'user_friends'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'FIELDS': [
             'id',
             'email',
             'name',
             'first_name',
             'last_name',
             'verified',
             'locale',
             'timezone',
             'link',
             'gender',
             'updated_time'],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'kr_KR',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v2.4'},
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True},
    'linkedin': {
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress'
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]}
}

# ___________________
# End of Social Login
# ___________________

# Jet admin theme
JET_SIDE_MENU_COMPACT = True

JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'light-blue',
        'color': '#1e72f6',
        'title': 'PT Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# DJ-STRIPE SETTINGS
STRIPE_LIVE_SECRET_KEY = env.str("STRIPE_LIVE_SECRET_KEY", "")
STRIPE_TEST_SECRET_KEY = env.str("STRIPE_TEST_SECRET_KEY", "")
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = env.str("DJSTRIPE_WEBHOOK_SECRET", "")
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

STRIPE_API_KEY = STRIPE_LIVE_SECRET_KEY
if not STRIPE_LIVE_MODE:
    STRIPE_API_KEY = STRIPE_TEST_SECRET_KEY
