from django.urls import path
# django는 명시적으로 경로를 표시한다.
from . import views

# app name 역시 설정 해 줬었다.
app_name = 'articles'

urlpatterns = [
    # path_name 이란 것을 설정 해 줘야 한다.
    # 물론, 필수는 아님.
    path('', views.index, name='index'),
    # 게시글 생성을 위해 필요한 게시글 생성 페이지
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # 수정한다 -> 뭘? 1번 게시글을 수정한다.
    # 무슨 게시글인지 알려 줘야 한다.
    # update/1/ -> 그 1이라는 값을 어떤 변수에 담을 것이다.
    path('update/<int:article_pk>/', views.update, name='update'),
]