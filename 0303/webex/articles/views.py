from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    # throw라는 html 파일은 어디에 있느냐?
    # django에서 모든 template은 각 app의 templates 폴더에 만든다.
    return render(request, 'articles/throw.html')

def catch(request):
    # print(dir(request))
    print('='*30)
    print(request.method)
    print(request.GET.get('message'))
    print('='*30)
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)