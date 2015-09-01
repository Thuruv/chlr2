from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }
