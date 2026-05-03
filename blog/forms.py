from django import forms #ModelForm을 사용하기 위해 import 

from .models import Post #view

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',) 