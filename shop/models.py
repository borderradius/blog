from django.db import models
from django.conf import settings

'''
프로젝트 내의 settings.py는 재정의된 내용들만 명시된 것이고.
기본 settings는 django/conf/global_setting.py 내에 있음.
'''

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop_post_set')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
