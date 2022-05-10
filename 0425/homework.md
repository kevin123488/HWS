## 0425 Homework

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.
- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한
  차이점은 변수의 유효범위이다. `F` ``

- “값이 없음”을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산
  자에서 undefined가 반환된다. `F` `null의 타입은 object가 출력됨`

- for ... in 문은 배열의 요소를 직접 순회하므로 배열의 각 요소를 활용하는 경우에 주로
  활용한다. `F` `배열의 요소를 직접 순회하는 것은 for of문` 

  `for in은 object인 경우 key, 배열인 경우 인덱스의 번호가 전달됨` `배열도 key와 value로 이루어진 object. 그러므로 순서를 보장하지 않음 -> 배열순회에는 권장하지 않음`

- ‘==’ 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 
  아니면 false를 반환한다 `F` `일치 비교 연산자 ===가 값과 타입 모두를 비교`

`동등 연산자 ==는 형변환이 가능하다면 자동 형변환 후 값이 같은지 확인함`





2. 아래 같이 numbers 배열이 주어졌을 때, 아래 요구사항들에 맞도록 코드를 작성하시오.

```javascript
const numbers = [1, 2, 3, 4, 5]
```

- for … of 문을 사용하여 배열의 각 요소를 출력하시오. 

```javascript
// ans
for (let i of numbers) {
    console.log(i)
}
```



- for … of 문을 사용하여 배열의 각 요소에 10을 더한 요소들로 구성된 새로운 배열을 생
  성하시오.

```javascript
// ans
let arr = []
for (let a of numbers) {
    a += 10
    arr.push(a)
}
arr
```



- for … of 문을 사용하여 배열의 각 요소들 중 홀수 요소 들로만 구성된 새로운 배열을 생
  성하시오.

```javascript
// ans
let arr = []
for (let a of numbers) {
    if (a%2 !== 0) {
        arr.push(a)
    }
}
arr
```



- for … of 문을 사용하여 배열의 각 요소들을 모두 더한 값을 구하시오

```javascript
// ans
let ans = 0
for (let a of numbers) {
    ans += a
}
ans
```



**const와 let에 대한 사실**

`const는 재선언, 재할당 불가`

`let은 재할당 불가`

`이를 값을 조작하는 행위 또한 불가하다고 생각하면 안된다`

`가령 const로 선언한 변수를 조작하여 값을 낸다고 치자`

```javascript
const arr = []
arr.push(1)
consol.log(arr)
```

`위의 코드는 문제없이 작동한다`

`왜? const로 선언한 []에 다른 값이, 조작이 가해졌는데 괜찮은 이유가 뭐야?`

`재할당이 뭐냐? 재할당은 =를 이용해 이미 할당된 값이 있는 변수에 다른 값을 넣어주는 것을 의미한다`

`위의 .push()는 재할당이 아니잖아? 그래서 괜찮음`

**다른 예시**

```javascript
const a = [1, 2, 3]
a = [3] // 재할당이므로 안됨

a[1] = 2 // 재할당이 아닌 값의 조작이므로 가능
```

