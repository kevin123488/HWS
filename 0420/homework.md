# HomeWork
### RESTful API

아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. `T`
- HTTP Method는 GET과 POST 두 종류 뿐이다. `F`
- ‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.



### status code

다음의 HTTP status code의 의미를 간략하게 작성하시오.

- 200: `요청이 성공적으로 되었다`
- 400 `잘못된 문법으로 인해 서버가 요청을 이해할 수 없음`
- 401 `비인증. 클라이언트는 요청한 응답을 받기 위해 반드시 스스로를 인증해야 함`
- 403 `클라이언트가 콘텐츠에 접근할 권리를 갖고 있지 않음`
- 404 `서버가 요청받은 리소스를 찾을 수 없을 때`
- 500 `서버가 처리 방법을 모르는 상황이 발생했을 때`



### ModelSerializer

아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

```python
class Student(models.Model):
    name = models.TextField()
    age = models.CharField(max_length=20)
    address = models.Textfield()
```

```python
class StudentSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
```





### Django REST Fraomework

Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

`ans: Serializers는 쿼리셋이나 모델 인스턴스들과 같은 복합적인 데이터를 python datatypes(json이나 xml 등과 같은 타입의 컨텐츠로 쉽게 랜더 가능한)으로 전환시켜주는 역할을 한다.`