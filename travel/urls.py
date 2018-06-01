from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect

# def root(request):
#     return redirect('blog:post_list')

urlpatterns = [
    # url(r'^$', root, name='root'),
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'), # root 함수 이용해서 url(r'^$', root, name='root') 로 개발하는것과 같은 효과. lambda 이용.
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')), # namespace 를 지정해주므로써 다른 앱의 동일한 url name을 구분 지을수 있다. blog:post_list , shop:post_list   include에 대한 namaspace이므로 헷갈리지 말것.
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
