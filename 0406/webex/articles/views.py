from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # print(dir(request))
    # print(request)
    '''
    모든 게시글 정보 조회
    ORM
    Model.manager.query API
    '''
    articles = Article.objects.all()
    # print(articles[0])
    # <Article object(0))> -> 제목
    context = {
        'articles': articles
    }
    # return render(request, 'index.html')
    return render(request, 'articles/index.html', context)

# def new(request):
#     form = ArticleForm()
#     # print(form)
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)

def create(request):
    if request.method == 'POST':
        # 게시글 생성 및 저장
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, '게시글이 생성되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    # print(form)
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def update(request, article_pk):
    # 특정 게시글 하나를 지정해서 수정
    # get query API는 단 하나의 객체를 조회 하고자 할 때 사용한다.
    # 대신, 2개 이상의 값이 조회 되거나 
    # 조회하는 대상이 없으면 오류가 발생한다.
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    # print(form)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)
