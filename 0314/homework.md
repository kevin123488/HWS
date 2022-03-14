# HomeWork
### SQL 용어 및 개념

아래의 보기에서 각 문항의 설명에 맞는 용어를 고르시오.

```html
보기: 기본 키, 테이블, 스키마, 레코드, 컬럼
```



1) 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것: `스키마`
2) 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합: `테이블`
3) 고유한 데이터 형식이 지정되는 열: `컬럼`
4) 단일 구조 데이터 항목을 가리키는 행: `레코드`
5) 각 행의 고유 값: `기본 키`



### SQL 문법

아래의 보기 (1) ~ (4) 중에서, DML이 아닌 것을 고르시오.

1. CREATE : answer. CREATE는 DML이 아닌 DDL이다.
2. UPDATE
3. DELETE
4. SELECT



### Relational DBMS

RDBMS의 개념적 정의와 이를 기반으로 한 DB-Engine의 종류 세가지 이상 작성하시오

RDBMS: 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

MySQL, SQLite, ORACLE . . .



### INSERT INTO 

다음과 같은 스키마를 가지는 테이블이 있을 때, 아래의 보기 (1) ~ (4) 중 틀린 문장을 고르시오. 

```sqlite
CREATE TABLE classmates (
	name TEXT,
    age INT,
    address TEXT
);
```

1. INSERT INTO classmates (name, age, address) VALUES(‘홍길동’, 20, ‘seoul’); 
2. INSERT INTO classmates VALUES(‘홍길동’, 20, ‘seoul’);
3. insert into classmates values(address=‘seoul’, age=20, name=‘홍길동’);
4. insert into classmates (address, age, name) values(‘seoul’, 20, ‘홍길동’);

**ans for 4:** 2

### 와일드카드 문자 

SQL에서 사용 가능한 와일드카드 문자인 %와 _을 비교하여 작성하시오.

**ans for 5:** %는 그 자리에 있을수도 있고 없을수도 있는 경우에 사용하고, _는 반드시 그 자리에 값이 존재할 경우 사용한다.