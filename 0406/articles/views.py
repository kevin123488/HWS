from django.shortcuts import render
from .models import Article # models라는 모듈에서 Article라는 클래스를 받아오자
from .forms import ArticleForm

# Create your views here.
def index(request):
    # request.POST
    # request.GET
    # return render(request, 'index.html')
    # 모든 게시글 정보 조회
    # Model.manager.query API
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)