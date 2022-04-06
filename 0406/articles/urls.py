from django.urls import path
# django는 명시적으로 경로 표시
from . import views

# app name 역시 설정
app_name = 'articles'

urlpatterns = [
    # path_name 이라는 것을 설정 해 주어야 한다
    # 필수는 아님. 근데 하면 좋다
    path('', views.index, name='index'),
    # 게시글 생성을 위해 필요한 게시글 생성 페이지
    path('new/', views.new, name='new'),
]