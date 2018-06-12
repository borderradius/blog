from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django import forms
from .forms import PostForm
from django.views.generic import ListView
from django.contrib import messages



# Create your views here.
def post_list(request):

    print(request.user.is_authenticated)
    print(request.user)

    qs = Post.objects.all()
    q = request.GET.get('q', '')
    # post_list = ListView.as_view(model=Post, paginate_by=10)
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q':q,
        # 'pagination': post_list,
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

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 글이 등록되었습니다람쥐.')
            return redirect(post) # post.get_absolute_url() => post detail
    else:    
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form':form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '글을 수정하였습니다.')
            return redirect(post) # post.get_absolute_url() => post detail
    else:    
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form':form,
    })

def comment_list(request):
    # comment_list = Comment.objects.all()
    comment_list = Comment.objects.all().select_related('post') # 외래키, OneToOne 관계일때 쿼리갯수를 줄일수있다.
    return render(request, 'blog/comment_list.html', {
        'comment_list': comment_list,
    })