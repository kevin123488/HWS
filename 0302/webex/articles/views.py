from django.shortcuts import render

# Create your views here.
# django의 모든 view 함수들은 기본적으로
# request 인자를 첫번째 인자로 받는다.
def index(request):
    # request라는 곳에는 무엇이 들어있을까???
    # print(dir(request))
    # 단, django에서 templates 파일들은 모두 app/templates 폴더에 들어있다.
    # render 함수의 2번째 인자, 파일명은 정확하게는
    # 파일 경로입니다. templates가 생략된
    return render(request, 'index.html')

def webex(request):
    foods = ['짜장면', '짬뽕', '탕수육']
    fruits = ['딸기', '바나나', '토마토는 과일이 아님']
    # 가장 기본 적인 형태
    # return render(request, 'webex.html', {'foods': foods, 'fruits': fruits})
    context = {
        'foods': foods,
        'fruits': fruits
    }
    return render(request, 'webex.html', context)
