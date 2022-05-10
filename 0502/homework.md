# HomeWork

### AJAX T/F

아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다. `T`
- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이
완료되면 Call Stack에 바로 할당된다. `F` `작동 순서는 callstack -> web api -> task queue -> event loop를 통해 call stack이 비었을 때 선입선출 되어 call stack으로 할당됨`



### asynchronous & synchronous

JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

`비동기: 병렬적 Task 수행. 요청 후 응답을 기다리지 않고 다음 동작이 이루어짐`

`동기: 순차적, 직렬적 Task 수행. 요청 후 응답을 받아야만 다음 동작이 이루어짐`



1. 동기 함수
   - 자바스크립트는 싱글 스레드이기 때문에 한번에 하나의 작업밖에 수행할 수 없다
   - 따라서 A작업 완료 후 B 작업을 진행하는 방식을 동기적 작동이라고 한다
2. 비동기 함수
   - 자바스크립트는 비동기 함수를 실행하게 되면 web api에게 실행 주체를 넘겨준다
   - 넘겨준 비동기 함수가 처리가 끝나기를 기다리는 것이 아니라, 본인이 해야 할 다음 작업으로 넘어간다



### Axios

다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오. `정상적으로 응답이 왔을 때? -> then으로 그 후의 수행을 코드로 나타낼 수 있다`

```js
axios.__(a)__('https://api.example/com/data')
	.__(b)__(function (response) {
	    console.log(__(c)__)
	})
```

`(a): get`

`(b): then`

`(c): response.data`
