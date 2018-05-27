# blog/models.py
from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100) # 길이제한이 있는 문자열
    content = models.TextField() # 길이제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
