# HomeWork
**한국어로 번역하기**

**1-1 django 프로젝트를 한국어로 제공하기 위해 번역이 필요하다. 이 설정을 위해 settings.py에 어떤 변수 그리고 어떤 값을 할당해야 하는지 작성하시오**

ans: LANGUAGE_CODE = 'ko-kr'

**1-2 추가로 settings.py에 ‘이 변수‘가 활성화인 상태여야 1-1번 변수를 설정할 수 있다고 한다. ‘이 변수’는 무엇인가?’**

ans: USE_I18N = True



**경로 설정하기**

**다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때 실행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 (a)에 추가되어야 할 코드를 작성하시오.**

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path(__a__),
    path('admin/', admin.site.urls),
]
```

ans: 'ssafy/', views.ssafy, name='ssafy'



**장고 template language**

1) **menus 리스트를 반복문으로 출력**

ans: menu

```django
{% for __a__ in menus %}
	<p>{{ menu }}</p>
{% endfor %}
```

2. **posts 리스트를 반복문을 활용하여 0번글부터 출력하시오**

ans: forloop.counter0

```django
{% for post in posts %}
	<p>
        {{ __a__ }}번 글: {{ post }}
	</p>
{% endfor %}
```



3. **user 리스트가 비어있다면 현재 가입한 유저가 없습니다 텍스트 출력**

```django
{% for user in users %}
	<p>{{ user }}</p>
{% __a__ %}
	<p>현재 가입한 유저가 없습니다</p>
{% endfor %}
```

ans: empty



4. **첫번째 반복문일 때와 아닐 때를 조건문으로**

ans:

```django
{% for ?? in ??? %}
	{% if forloop.first %}
		<p>첫번째 반복문 아닙니다</p>
	{% endif %}
{% endfor %}
```

5. 출력된 결과가 주석과 같아지도록 하시오

```django
<!--5-->
<p>{{ 'hello'|__a__ }}</p>
<!--My Name Is Tom-->
<p>{{ 'my name is tom'|__b__ }}</p>
```

a: length

b: title



6. **변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오**

```django
<!-- 2020년 02월 02일 (Sun) PM 02:02-->
{{ today|date:"__a__" }}
```

a: Y년 m월 d일 (D) A h:i



7. **form tag with django**

```django
```

**(1): action**-> form태그의 데이터를 보낼 위치를 지정한다

**(2): method가 가질 수 있는 속성값**-> GET, POST

**(3): input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고**
**submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.**

ans: https://127.0.0.1:8000/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅