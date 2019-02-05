from django import forms

from .models import Post


class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('id', 'slug')
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

