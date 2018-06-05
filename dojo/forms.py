# dojo.forms.py

from django import forms
from .models import Post






class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__' # model에 정의된 모든 필드를 다 가져옴.
        fields = ['title','content']




# class PostForm(forms.Form):
    # title = forms.CharField(validators=[min_length_3_validator])
    # content = forms.CharField(widget=forms.Textarea) 

    # model forms 를 이용한 방법
    # def save(self, commit=True):
    #     post = Post(**self.cleaned_data)
    #     if commit:
    #         post.save()
    #     return post


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
        # post = Post.objects.create(**form.cleaned_data)  # form.cleaned_data 는 사전이므로 ** 로 언팩해서 넣을 수 있음. 