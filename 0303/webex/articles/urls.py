from django.urls import path
# 단, django에서는 명시적 경로를 작성해 주어야 한다.
from . import views

urlpatterns = [
    path('index/', views.index),
    path('throw/', views.throw),
    path('grab/', views.catch),
    # < datatype : variable_name >
    # name = '김구현'
    path('hello/<str:name>/', views.hello),
]