## 0510 HW

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.
- Vue는 컴포넌트 간 양방향 데이터 흐름을 지향하기 때문에
부모, 자식 컴포넌트 간의 데이터 전달 및 수정이 자유롭다. `F`
- v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시
전달받은 함수를 실행한다. `T`
- 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 이벤트를 보내고,
자식 컴포넌트는 emit을 통해 부모 컴포넌트에게 데이터를 전달한다 `F`



2. Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크다.
공식문서를 참고하여 그 이유를 서술하시오. 

https://kr.vuejs.org/v2/guide/components.html#_bsa_srv-CKYD62QM_0

`ans: 상위 속성이 업데이트되면 하위속성에 해당 정보가 반영되는 과정을 거치는것은 괜찮다. 그러나 하위 속성의 데이터 변화가 상위속성에 변화를 야기하는것은 문제가 될 수 있으므로 단방향 데이터흐름을 지향하는 것`



3. 아래와 같은 Vue 프로젝트에서 2개의 버튼이 동작하는 것을 비교하여
  .native 수식어의 역할을 작성하시오.

  `ans: 작성해서 돌려봤는데, 잘 모르겠다... .native를 달아준 건 잘 작동이 되는 데 안달아준건 작동이 안된다. 왜일까`

  ```vue
  // App.vue
  
  <template>
  	<div id="app">
          <hello-world @click="onClick"></hello-world>
          <hello-world @click.native="onClick"></hello-world>
      </div>
  </template>
  
  <script>
  import HelloWorld from '@/components/HelloWorld.vue'
      
  export default {
      name: 'App',
      components: {
          HelloWorld,
      },
      methods: {
          onClick: function() {
              console.log('Hello')
          }
      }
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  // HelloWorld.vue
  
  <template>
  	<div>
          <button>버튼</button>
      </div>
  </template>
  
  <script>
  export default {
      name: 'HelloWorld',
  }
  </script>
  ```

  



4. 다음은 자식 컴포넌트에서 이벤트를 발생시켜 부모 컴포넌트의
  함수를 실행하는 코드이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.
  • TodoListInput 컴포넌트의 버튼을 누르면 add-todo 이벤트가 발생한다. 
  (이벤트 발생 시 data의 inputData 값도 함께 전달한다.)
  • TodoList 컴포넌트에서 add-todo 이벤트를 청취하면, 
  onAddTodo 메서드를 실행한다.
  • onAddTodo 메서드에서는 TodoListInput 컴포넌트에서 전달받은 값을
  console.log 함수를 통해 출력한다.

  `ans`

  (a): this.$emit

  (b): @add-todo="onAddTodo"

  (c): onAddTodo: function(inputData) {

  ​	console.log(inputData)

  }

  ```vue
  // TodoListInput.vue
  
  <template>
  	<div>
          <input type="text" v-model="inputData">
          <button @click="onClick">추가</button>
      </div>
  </template>
  
  <script>
  export default {
      name: 'TodoListInput',
      data: function() {
          return {
              inputData: '',
          }
      },
      methods: {
          onClick: function() {
              __(a)__('add-todo', this.inputData)
          },
      },
  }
  </script>
  ```

  ```vue
  // TodoList.vue
  
  <template>
  	<div>
          <todo-list-input __(b)__ ></todo-list-input>
      </div>
  </template>
  
  <script>
  export default {
      name: 'MyTodoList',
      components: {
          TodoListInput,
      },
      methods: {
          __(c)__
      }
  }
  </script>
  
  <style>
  
  </style>
  ```

  