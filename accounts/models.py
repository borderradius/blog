# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    # user = models.ForeignKey('auth.User') # 비추천방식
    # user = models.OneToOneField(User) # 비추천방식
    user = models.OneToOneField(settings.AUTH_USER_MODEL) 
    # 추천방식
    # 장고 사용자 인증에 사용되는 User 모델 변경을 지원

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
