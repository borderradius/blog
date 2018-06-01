# blog/models.py
import re
from django.forms import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    # related_name='+' -> related_name을 포기한다는 것.
    # shop모델과 related_name이 충돌나는것을 포기. 충돌나는 이름을 각각 재정의 해주거나 포기해야함.


    # author = models.CharField(max_length=20)
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
    tag_set = models.ManyToManyField('Tag', blank=True) # 문자열로 클래스명을 지정해주면 릴레이션을 맺는 클래스가 같은 앱안에 있다고 판단함. 다른 앱의 모델과 릴레이션을 건다면 ? 'auth.Tag' 로 사용 
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

    # 쿼리내 기본정렬은 모델 내 Meta.ordering 설정에 따름.
    class Meta: 
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id]) # detail 로 이동할때 유용하다. 새글을 작성하거나 수정했을때는 상세페이지를 보여주는것이 당연한 시나리오.

# 댓글모델
class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name