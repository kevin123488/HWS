[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```



---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   
   User.objects.all()
   ```

      ```sql
   -- sql
   
   SELECT * FROM users_user;
   # 이번 실습에서의 테이블 이름은 users_user
      ```

2. user 레코드 생성

   ```python
   # orm
   
   user = User() # 이번 실습에서의 class이름은 User
   user.first_name = '싸피'
   user.last_name = '폰'
   user.age = 28
   user.country = '경상남도'
   user.phone = '010-1212-1221'
   user.balance = 10000
   user.save()
   ```

   ```sql
   -- sql
   
   INSERT INTO users_user (first_name, last_name, age, country, phone, balance) VALUES ('정현', '박', '20', '경상남도', '010-1234-1234', '12312315352')
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   
   User.objects.get(pk=102)
   ```

   ```sql
   -- sql
   
   SELECT * FROM users_user WHERE id=102;
   # SELECT * FROM users_user LIMIT 1 OFFSET 101;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   
   user1 = User.objects.get(pk=102)
   user1.last_name = '김'
   user1.save()
   ```

      ```sql
   -- sql
   
   UPDATE users_user SET first_name='철수' WHERE id=102;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   
   user = User.objects.get(pk=102)
   user.delete()
   ```
   
   ```sql
   -- sql
   
   DELETE FROM users_user WHERE id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   
   user = User.objects.all()
   len(user)
   ```

   ```sql
   -- sql
   
   SELECT COUNT(*) FROM users_user;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   
   User.objects.filter(age=30).values('first_name')
   # 첫번째 괄호엔 조건을, 두번째 괄호엔 출력해줄 컬럼을 작성한다. 두번쩨 값은 ''안에 작성
   ```

      ```sql
   -- sql
   
   SELECT first_name FROM users_user WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   
   user = User.objects.filter(age__gte=30).values('first_name')
   len(user)
   ```

      ```sql
   -- sql
   
   SELECT COUNT(*) FROM users_user WHERE age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   
   user = User.objects.filter(age__lte=20).values('first_name')
   len(user)
   ```

   ```sql
   -- sql
   
   SELECT COUNT(*) FROM users_user WHERE age<=20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   
   len(User.objects.filter(last_name='김', age=30))
   ```

      ```sql
   -- sql
   
   SELECT COUNT(*) FROM users_user WHERE age=30 AND last_name='김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   
   user = User.objects.filter(last_name='김')|User.objects.filter(age=30)
   len(user)
   ```

   ```sql
   -- sql
   
   SELECT COUNT(*) FROM users_user WHERE age=30 OR last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수 **% 쓰는법 잘 알아두기**

   - `ORM`: `__startswith` 

   ```python
   # orm
   
   user = User.objects.filter(phone__startswith='02')
   len(user)
   ```

      ```sql
   -- sql
   
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   
   User.objects.filter(country='강원도', last_name='황').values('first_name')
   ```
   
      ```sql
   -- sql
   
   SELECT first_name FROM users_user WHERE country='강원도' AND last_name='황';
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   
   SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   
   SELECT * FROM users_user ORDER BY balance ASC LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   
   User.objects.order_by('balance', '-age')[:10]
   ```
   
   ```sql
   -- sql
   
   SELECT * FROM users_user ORDER BY balance ASC, age DESC LIMIT 10;
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   
   User.objects.order_by('-last_name', '-first_name')[4]
   ```
   
      ```sql
   -- sql
   
   SELECT * FROM users_user ORDER BY last_name, first_name DESC LIMIT 1 OFFSET 4;
      ```



---



### 4. 표현식

#### 4.1 Aggregate

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

   ```python
   # orm
   
   User.objects.all().aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   
   SELECT AVG(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   
   SELECT AVG(age) FROM users_user WHERE last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   ```

   ```sql
   -- sql
   
   SELECT AVG(balance) FROM users_user WHERE country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   
   user = User.objects.order_by('-balance')[0]
   user.balance
   ```

      ```sql
   -- sql
   
   SELECT balance FROM users_user ORDER BY balance DESC LIMIT 1 OFFSET 0;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   
   User.objects.aggregate(Sum('balance'))
   ```
   
      ```sql
   -- sql
   
   SELECT SUM(balance) FROM users_user;
      ```



#### 4.2 Annotate

1. 지역별 인원 수

   ```PYTHON
   # orm
   
   USer.objects.values('country').annotate(Count('country'))
   ```
   
   ```SQL
   -- sql
   
   SELECT country, COUNT(country) FROM users_user GROUP BY country;
   # country, COUNT(country)를 해주지 않으면 count된 값만 덩그러니 출력됨
   ```
   
   