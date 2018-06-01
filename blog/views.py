from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q':q,
    })

def post_detail(request, id):
    # 404 에러를 위한코드
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:  
    #     raise Http404
    # 하지만 위 코드는 너무 번거로움

    # 위의 4줄가 같은코드, 특정 조건에 맞는 인스턴스 획득시에는 이걸 사용하도록
    post = get_object_or_404(Post, id=id)


    return render(request, 'blog/post_detail.html',{
        'post': post,
    })


    # http 200 응답
    # return HttpResponse()
    # return render()
    # return JsonResponse()

    # http 302 응답
    # return HttpResponseRedirect('/blog/)
    # return HttpResponseRedirect(url) # url reverse 
    # return redirect('blog:post_list')

    # http 404 응답
    # 1. raise Http404
    # 2. post = get_object_or_404(Post, id=100) # 없는 id 일 경우 http404 예외 발생
    # 3. HttpResponseNotFound() # 잘 안쓰는 방법

    # http 500 응답
    # 서버에서 요청처리중에 예기치못한 오류(코드오류, 설정오류) 가 발생할 경우

