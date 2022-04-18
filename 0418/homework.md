# HomeWork
### M:N True or False

각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고, 틀렸다면 그 이유도 함께 작성하시오.

1) Django에서 1:N 관계는 ForeignKeyField를 사용하고, M:N 관계는 ManyToManyField를 사용한다. `T`
2) ManyToManyField를 설정하고 만들어지는 테이블 이름은 “앱이름_클래스이름_지정한 필드이름”의 형태로 만들어진다. `T`
3) ManyToManyField의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다. `F`



### Like in templates

아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

![image-20220418121742027](homework.assets/image-20220418121742027.png)

`ans: (a): user, (b): like_users`



### Follow in views

모델 정보가 다음과 같을 때 빈칸 a, b, c, d, e에 들어갈 코드를 각각 작성하시오.



![image-20220418121749234](homework.assets/image-20220418121749234.png)

![image-20220418121801859](homework.assets/image-20220418121801859.png)

`ans: (a): user_pk, (b): followers, (c): filter, (d): remove, (e): add`

### User AttributeError

다음과 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오.

![image-20220418121809315](homework.assets/image-20220418121809315.png)

`ans: `

### related_name

아래의 경우 ForeignKey 혹은 ManyToManyField에 related_name을 필수적으로 작성해야 한다. 그 이유를 설명하시오. 

![image-20220418121814987](homework.assets/image-20220418121814987.png)

`ans: 역참조시 이름을 설정해주지 않아 충돌이 일어날 수 있다.`