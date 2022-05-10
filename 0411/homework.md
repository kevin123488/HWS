# HomeWork
### Django User Model

- Django에서 기본적으로 사용하는 User 모델은 아래의 경로에서 찾아볼 수 있다.

  ```python
  from django.contrib.auth.models import User
  ```

-  아래의 Django 공식 github에서 User 모델이 정의된 코드를 찾아 작성하시오.
  https://github.com/django/django
  
- 모델은 class

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
```

User class에 직접적으로 field를 지정해둔것이 아닌 상속의 형태로 만들어 둔 이유는? -> 



### Create user by ModelForm

새 유저를 생성하는 Django 내부에 정의된 ModelForm을 사용하기 위한 import 구문을 작성하시오.

```python
from django.contrib.auth.forms import UserCreationForm
```





### Django sessions

Django는 사용자가 로그인에 성공할 경우 (a) 테이블에 세션 데이터를 저장한다.
그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 (b)다.
(a)와 (b)에 알맞은 값을 작성하시오.

```python
# (a): auth_user
# (b): ['_auth_user_id', '_auth_user_backend', '_auth_user_hash']
```

```python
# 교수님 답변
# (a): django_session
# (b): sessionid
```

세션: 연결관계를 지속하는 기간을 말하는 섬띵

서버와 클라이언트는 기본적으로 연결되어있지 않음. 특정한 기간동안만 그 연결을 확인할 수 있는데, 그 기간과 관계되어 있는 것이 session

**연결되어있는 상태**
