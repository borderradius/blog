# blog/admin.py
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size','created_at', 'updated_at']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'
    '''
    list_display_links : 목록 내에서 링크로 지정할 필드 목록. 이를 지정하지 않으면 첫번째 필드만 링크가 적용
    list_editable : 목록상에서 수정할 필드 목록
    list_per_page : 페이지별로 보여질 최대 갯수, 디폴트 100
    list_filter : 필터옵션을 제공할 필드목록
    actions : 목록에서 수행할 action 목록
    위에 까지는 쉽게 사용가능.

    fields : add/change 폼에 노출할 필드 목록
    fieldsets : add/change 폼에 노출할 필드 목록
    formfield_overrides : 특정 form field에 대한 속정 재정의
    form : 디폴트로 몯레 클래스에 대한 form class지정
    '''

# admin.site.register(Post, PostAdmin)  
# 위 코드는 @admin.register(Post) 어노테이션과 같은 기능. 
