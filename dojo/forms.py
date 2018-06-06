# dojo.forms.py

from django import forms
from .models import Post






class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__' # model에 정의된 모든 필드를 다 가져옴.
        fields = ['title','content','user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }



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


        #** request.POST['message'] 말고 form.cleaned_data['message']를 이용하자.
        # request.POST 는 원시데이터. - 띄어쓰기 제대로 안되어 있을수도있음.
        # form.cleaned_data 는 유효성 검사를 통과한 값들임.