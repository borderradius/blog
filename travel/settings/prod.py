from .common import *

ALLOWED_HOSTS = ['*']
# 실 서비스에 사용되는 도메인 적을 것.

DEBUG = False
# ORM 쿼리 실행내역이 메모리에 누적되지 않는다.
# 메모리 누적 -> 부족 -> 서비스 불능
# 예외발생시 유저에게 노출되지 않는다.

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        # 'USER': 'db user name',
        # 'NAME': '데이터베이스 DB명'
        # 'PASSWORD': 'db password',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    # },
# }