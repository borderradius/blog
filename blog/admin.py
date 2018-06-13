# blog/admin.py
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['make_published','make_draft']
    list_display = ['id', 'title', 'tag_list', 'content_size','status','created_at', 'updated_at']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    def tag_list(request, post):
        return ', '.join(tag.name for tag in post.tag_set.all()) # list comprehension문법  

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

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') # QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count)) # django message framework 활용
    make_published.short_description = "저정포스팅을 Published로 변경"
    
    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') # QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count)) # django message framework 활용
    make_draft.short_description = "저정포스팅을 Draft로 변경"

# admin.site.register(Post, PostAdmin)  
# 위 코드는 @admin.register(Post) 어노테이션과 같은 기능. 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','post_content_len']
    
    # list_select_related = ['post']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('post')

    def post_content_len(self, comment):
        return '{}글자'.format(len(comment.post.content))

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']