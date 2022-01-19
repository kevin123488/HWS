## Homework3

1. **Built-in 함수**
**Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.**

**ans for 1:**

```python
print(), sum(), abs(), len(), int(), float() . . .
```





2. **정중앙 문자**
**문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다**

```python
get_middle_char('ssafy') #=> a
get_middle_char('coding') #=> di
```

**ans for 2:**

```python
def get_middle_char(string):
    if len(string) % 2:
        return string[len(string)//2]
    else:
        return string[len(string)//2-1], string[len(string)//2]
```





3. **위치 인자와 키워드 인자**
**다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는 코드를 고르시오.**

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')

# (4)
ssafy(name='길동', '구미')
```

**ans for 3:** (4)

```python
# 파라미터 선언시 주의할 점
# 디폴트 파라미터는 반드시 '뒷쪽'에 위치해야 한다.
# 헷갈릴 땐 print()를 생각해보자
# print()의 디폴트 파라미터인 end = '\n'의 경우, end = ''를 넣어줌으로써 지정된 값을 바꿀 수 있었다. 이와 같은 논리로 2, 3번은 ok라고 볼 수 있다.
# 1번의 경우, print()에 하나의 값을 입력한것과 같은 상황이다. 그러므로 ok
```

다시, **default parameter**는 **반드시 뒷쪽**에 위치해야 한다.

**argument**또한 마찬가지.

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
# 모든 케이스 정리
#1.
ssafy('가나')
# 위의 경우 name에 '가나', location엔 디폴트인 '서울'이 들어감. 옳은 코드

#2.
ssafy('다라', '부산')
# 위의 경우 name에 '다라', location에 '부산'이 들어감. 옳은 코드
# 컴퓨터가 '다라'와 '부산'의 순서가 각각 name과 location이라는 것을 알기 때문에, 들어갈 수 있음

#3.
ssafy('거너', location = '부산')
# 위의 경우 keyword argument가 뒤로 가있으므로 잘 돌아감. 옳은 코드

#4.
ssafy(name = '마바')
# 위의 경우 name에 '마바'가 지정되어 잘 들어감. 옳은 코드

#5.
# ssafy(name = '사아', '부산')
# 위의 경우 'keyword argument가 positional argument보다 앞에 있으므로' 안 돌아감. 잘못된 코드

#6.
ssafy(name = '자차', location = '부산')
# 위의 경우 둘 다 keyword argument라 잘 돌아감. 옳은 코드
```





4. **나의 반환값은**
**다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.**

```python
def my_func(a, b):
    c = a + b
    print(c)
    
result = my_func(3, 7)
```

**ans for 4:**

```python
None
```







5. **가변 인자 리스트**
**가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정수들의 평균 값을 반환하는 my_avg 함수를 작성하시오**

```python
my_avg(77, 83, 95, 80, 70) #=> 81.0
```

**ans for 5:**

```python
def my_avg(*num):
    su_m = 0
    for i in num:
        su_m += i
    return su_m/len(num)

result = my_avg(77, 83, 95, 80, 70)
print(result)
```

