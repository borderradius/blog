# blog/models.py
import re
from django.forms import ValidationError
from django.db import models

# [+_]?  정규표현식에서 ?는 0회 혹은 1회 출현을 의미함. 없거나 혹은 한번 나오거나. 
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    title = models.CharField(max_length=100) # 길이제한이 있는 문자열
    content = models.TextField() # 길이제한이 없는 문자열
    tags = models.CharField(
        max_length=100, 
        blank=True)
    lnglat = models.CharField(
        max_length=50, 
        blank=True, # 값이 없어도 저장됌. 필수값이 아니라는 뜻.
        help_text='경도, 위도 포맷으로 입력',
        validators=[lnglat_validator])
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)    
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 최초생성시 자동으로 들어감.
    updated_at = models.DateTimeField(auto_now=True) # auto_now 레코드 생성시 자동으로 들어감.

    # choices
    # title1 = models.CharField(max_length=100,
    #     choices = (
    #         ('디비에 저장될 값1', 'ui에 보여질 레이블'),
    #         ('디비에 저장될 값2', 'ui에 보여질 레이블'),
    #         ('디비에 저장될 값3', 'ui에 보여질 레이블'),
    #     ))
    
    # 입력값을 좌우 공백 제거 strip 옵션