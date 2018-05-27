# blog/models.py
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # 길이제한이 있는 문자열
    content = models.TextField() # 길이제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 최초생성시 자동으로 들어감.
    updated_at = models.DateTimeField(auto_now=True) # auto_now 레코드 생성시 자동으로 들어감.

    # choices
    # title1 = models.CharField(max_length=100,
    #     choices = (
    #         ('디비에 저장될 값1', 'ui에 보여질 레이블'),
    #         ('디비에 저장될 값2', 'ui에 보여질 레이블'),
    #         ('디비에 저장될 값3', 'ui에 보여질 레이블'),
    #     ))
    