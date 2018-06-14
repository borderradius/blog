from .common import *

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

# 각 media파일에 대한 URL Prefix
MEDIA_URL = '/media/' # 항상 /로 끝이 나도록 설정, url이 media로 들어오는가? 
# 현재 서버에서 서빙할 경우 : '/media/'
# 다른 서버에서 서빙할 경우 : 'https://도메인.com/media/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
# 업로드된 파일을 저장할 디렉토리 경로, 절대경로로 지정하는 것이 좋음.