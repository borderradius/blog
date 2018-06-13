"""
Django settings for travel project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k@66=q@b*b^72pafnip)gcs*%_yo+8*l7%1@lz-j3m%n87y!&='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'blog',
    'dojo',
    'accounts',
    'shop',
    'bootstrap3',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'travel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'travel', 'templates'), # 여기에도 템플릿 파일이 존재하고 있다라는 걸 알려줘야함. filesystem.loader 프로젝트 전반적으로 쓰일 템플릿 파일은 "특정앱/templates/" 경로가 아닌 별도의 경로에 저장이 필요
        ],
        'APP_DIRS': True, # True로 두게되면 장고가 app_directories.loader에 추가를 해줌. app_directories.loader는 settings.INSTALLED_APPS 에 설정된 앱 디렉토리 내 templates경로에서 템플릿 파일을 찾는것
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # context_processors 의 역할
            # 모든 템플릿에서 사용하는 변수목록이 있는데 그런 변수들을 매번 뷰함수에서 하나하나 지정해서 넘기는건 번거로움.
            # 고로 context_processors에 등록해두면 뷰에서 넘기지 않고도 템플릿에서 접근해서 사용할 수 있다는 것.
        },
    },
]

WSGI_APPLICATION = 'travel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # ㅓㅕ'ENGINE': 'django.db.backends.mysql',
        # 'USER': 'db user name',
        # 'PASSWORD': 'db password',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/' 

# 최상위 정적인 파일의 위치설정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'travel', 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 각 media파일에 대한 URL Prefix
MEDIA_URL = '/media/' # 항상 /로 끝이 나도록 설정, url이 media로 들어오는가? 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 업로드된 파일을 저장할 디렉토리 경로

INTERNAL_IPS = ['127.0.0.1']

from django.contrib.messages import constants
MESSAGE_LEVEL = constants.DEBUG # 지금부터 debug레벨의 messages를 남길수있음.
MESSAGE_TAGS = {constants.ERROR: 'danger'}


# 기본 로그인 페이지 url지정
# login required 장식자 등에 의해서 사용
LOGIN_URL = '/accounts/login/'

# 로그인 완료 후에 get방식으로 next 인자가 지정되면 next의 url로 페이지이동
# next 인자가 없으면 아래 url로 이동
LOGIN_REDIRECT_URL = '/accounts/profile'

# 로그아웃 완료 후에
# - next_page 인자가 지정되면 next_page url 로 페이지 이동
# - next_page 인자가 없으면 LOGOUT_REDIRECT_URL 이 지정되었을 경우 그곳으로 이동
# - next_page 인자가 지정되지 않고 LOGOUT_REDIRECT_URL이 None 일 경우
#   redirect를 수행하지 않고 'registration/logged_out.html' 템플릿 렌더링
LOGOUT_REDIRECT_URL = None

# 인증에 사용할 커스텀 User 모델 지정, '앱이름.모델명'
AUTH_USER_MODEL = 'auth.User'