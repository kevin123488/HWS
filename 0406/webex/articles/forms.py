from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    # 엄청난거 아님
    # 메타 데이터 
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('content', )