# HomeWork
### MTV

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의
약자이며, 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는
역할을 간략히 서술하시오.

**ans for 1:**

```python
MTV: Model Template View
    Model(Model)-> 응용프로그램의 데이터 구조를 정의, 기록을 관리(조회, 생성, 수정, 삭제)
    Template(View)-> 파일 구조나 레이아웃 정의. 실제 내용을 보여주는데 사용
    View(Controller)-> HTTP 요청 수신 후 HTTP응답 반환. Model 통해 요청충족에 필요한 데이터에 접근.
    	   			   Template에게 응답의 서식 설정을 맡김

MVC: Model View Controller
```





### URL

__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을
의미한다. __(a)__는 무엇인지 작성하시오.

**ans for 2**

```python
variable routing
```





### Django template path

Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에
등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다.
__(a)__에 들어갈 폴더 이름을 작성하시오.

**ans for 3**

```python
templates
```

