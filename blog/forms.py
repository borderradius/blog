# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title','content','tags','lnglat','status','tag_set']
        fields = '__all__'