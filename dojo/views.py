from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

# request: HttpRequest
def mysum(request, x, y):
    return HttpResponse(int(x)+int(y))

def hello(request, name, age):
    return HttpResponse("안녕하세요. {}. {} 살이시네요 ".format(name, age))

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES) # 순서 바뀌면 안됌. 파일 안받으면 생략해도 됌.
        
        # 인자로 받은 값은 유효성 검증 수행
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') #namespace: name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post) # 순서 바뀌면 안됌. 파일 안받으면 생략해도 됌.
        
        # 인자로 받은 값은 유효성 검증 수행
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') #namespace: name
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html',{
        'form':form
    })