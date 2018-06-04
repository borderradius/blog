from django.shortcuts import render, redirect
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
            # 방법 1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법 2
            # post = Post(title=form.cleaned_data['title'],
            #             content=form.cleaned_data['content'])
            # post.save()

            # 방법 3
            # post = Post.objects.create(title=form.cleaned_data['title'],
            # content=form.cleaned_data['content'])

            # 방법 4
            post = Post.objects.create(**form.cleaned_data)  # form.cleaned_data 는 사전이므로 ** 로 언팩해서 넣을 수 있음. 

            return redirect('/dojo/') #namespace: name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form
    })