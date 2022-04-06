from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea) # template에서 어떻게 보여줄 것인가 -> widget

class ArticleForm(forms.ModelForm):
    class Meta: # 메타 데이터, 데이터를 위한 데이터
        model = Article
        fields = '__all__'
        # exclude = ('content', )