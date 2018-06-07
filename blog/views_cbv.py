from django.views.generic import CreateView
from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/'
    # get_absolute_url() 을 작성해놓으면 success_url 필요치 않아.

post_new = PostCreateView.as_view()