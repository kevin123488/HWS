# HomeWork

### HTML 정의

아래의 보기 (1) ~ (4) 중에서, HTML의 본딧말을 고르시오.

```
1. Hyperlinks and Text Markup Language
2. Home Tool Markup Language
3. Hyper Text Markup Language
4. Hyper Tool Markup Language
```

**ans for 1:**

```python
3. Hyper Text Markup Language
```



### HTML 개념

각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

```
1. 웹 표준을 만드는 곳은 Mozilla 재단이다.
2. 표(table) 을 만들 때에는 반드시 <th> 태그를 사용해야 한다.
3. 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다.
4. 리스트를 나열하기 위해서는 <ul> 태그만 사용 할 수 있다.
5. HTML의 태그는 반드시 별도의 닫는 태그가 필요하다.
```

**ans for 2:**

```python
1. 웹 표준을 만드는 곳은 모질라 재단이다 -> T
# 애플, 구글, 마이크로소프트 그리고 모질라 재단
# 정답 F. W3C과 WHATWG이 웹 표준을 만들고 있음. 모질라는 그 소속

2. 표(table) 을 만들 때에는 반드시 <th> 태그를 사용해야 한다. -> F
# 내부는 <th> 혹은 <td>로 셀을 구성 가능
# 정답 F. 반드시 th 태그를 사용할 필요는 ㄴ

3. 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. -> F
# 그런게 어딨냐
# 정답 T. 사용할 순 있는데, 제목 이외엔 사용하지 않는게 좋음. 어디까지나 '권장사항'

4. 리스트를 나열하기 위해서는 <ul> 태그만 사용 할 수 있다. -> F
# <u1>, <ol>, <dl> 모두 사용 가능. ol은 순서 있는 경우, ul은 순서 없는 경우, dl은 용어를 설명하는 경우 사용함
# 정답 F. ol, ul 모두 사용 가능. 순서 유무에 따라 바뀜. 각 리스트 아이템들은 li 태그를 사용해서 나타낸다.

5. HTML의 태그는 반드시 별도의 닫는 태그가 필요하다. -> F
# <br> 같은 애들은 별도의 닫는태그 필요 ㄴ
# 정답 F. 필요 없는 애들도 있음. + 한쌍이 하나에 들어가있는 애들도 있음. 'input', 'img' 등등...
```



### CSS 정의

아래의 보기 (1) ~ (4) 중에서, CSS의 본딧말을 고르시오.

```
1. Creative Style Sheets
2. Cascading Style Sheets
3. Computer Style Sheets
4. Colorful Style Sheets
```

**ans for 3:**

```python
2. Cascading Style Sheets
```





### CSS 개념

각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

```
1. HTML과 CSS는 각자 문법을 갖는 별개의 언어이다.
2. 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.
3. 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다.
4. 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.
5, id 값은 유일해야 하므로 중복되어서는 안된다.
```

**ans for 4:**

```python
1. HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. -> T
# 반드시 기억합시다

2. 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. -> T
# 정답 T.

3. 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다. -> F
# 일부 속성은 상속, 일부 속성은 상속 ㄴ
# 정답 F. width, height, background-color 등은 상속받지 않음.

4. 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다. -> T
# 정답 F. vw, vh 등의 viewport에 따른 상대단위가 별도로 존재한다

5. id 값은 유일해야 하므로 중복되어서는 안된다. -> F
# 중복돼도 되긴 됨. 중복시키지 않는걸 권장할 뿐
# 정답 T
```



## CSS 우선순위

CSS는 우선 적용되는 순서가 존재한다. 우선순위대로 나열 ㄱ

**ans for 5:**

```python
!important > Inline style > id 선택자 > class 선택자 > 요소 선택자 > 소스 순서
```

