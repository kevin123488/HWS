## Homework

**1. CSS flex-direction**

Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.

**ans for 1:**

```html
flex-direction: row;
-> 수평방향으로, 순서대로 정렬

flex-direction: row-reverse;
-> 수평방향으로, 역순으로 정렬

flex-direction: column;
-> 수직방향으로, 순서대로 정렬

flex-direction: column-reverse;
-> 수직방향으로, 역순으로 정렬
```



**2. Bootstrap flex-direction**

flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

**ans for 2:**

```html
d-flex flex-row
d-flex flex-row-reverse
d-flex flex-column
d-flex flex-column-reverse
```



**3. align-items**

align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

**ans for 3:**

```html
align-items: center
-> 요소들을 세로선 상의 중앙부에 위치시킴
교차축의 중앙에 정렬

align-items: flex-start
-> 요소들을 세로선 상의 최상단에 위치시킴
교차축 방향의 시작선에 정렬

align-items: flex-end
-> 요소들을 세로선 상의 최하단에 위치시킴
교차축 방향의 끝에 정렬

align-items: baseline
-> 요소들을 baseline에 맞춰 정렬

+

align-items: stretch
-> 요소들을 컨테이너에 맞게 늘림
부모 flex 컨테이너의 최대 높이로 설정
```



**4. flex-flow**

flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.

```html
(1) flex-direction, flex-wrap
(2) flex-direction, align-items
(3) justify-content, flex-wrap
(4) justify-content, align-items
```

**ans for 4:**

```html
(1)
```



**5. Bootstrap Grid System**

하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, (a), (b) 각각에 입력해야 할 클래스 이름을 작성하시오.

```html
<div class="(a)">
  <div class="(b)">
    <div class="col-(c)-(d)"></div>
  </div>
</div>
```

**ans for 5:**

```html
(a): container
(b): row
```

*container또한 breakpoint를 설정할 수 있다.



**6. Breakpoint prefix**

Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

1) (c)에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.
2) (d)에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.

**ans for 6:**

```html
1) xs, sm, md, lg, xl, xxl -> 디바이스나 화면의 크기에 따라서 반응형으로 디자인 구현 가능

2) 숫자(12이하의 정수) -> 공간을 12개로 나누어 해당 요소가 몇칸을 차지할 것인지를 정의
```

