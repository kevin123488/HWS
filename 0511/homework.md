## 0511 homework

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.
- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다. `F`
- mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다. `T`
- mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다. `F` `mutations는 commit으로, actions는 dispatch로 호출할 수 있다`
- state는 data의 역할, getters는 computed와 유사한 역할을 담당한다. `T`



2. Vuex에서 State, Getters, Mutations, Actions의 역할을 각각 서술하시오.

   `State: data`

   `Getters: computed`

   `Mutations: change`

   `Actions: change이외 모든 function`



3. 컴포넌트에 작성된 Todo App 관련 코드를 Vuex의 Store로 옮기고자 한다. 
  빈 칸 (a), (b), (c), (d)에 들어갈 코드를 작성하시오.

  ```vue
  export default {
  	name: 'TodoList',
  	data: function() {
  		return {
  			todoList: [],
  			status: 'all',
  		}
  	},
  	computed: {
  		todoListByStatus: function() {
  			return this.todoList.filter((todo) => {
  
  			})
  		},
  	},
  	methods: {
  		addTodo: function() {
  			
  		},
  	},
  }
  ```

  ```vue
  export default new Vuex.Store({
  	__(a)__ {
  		todoList: [],
  		status: 'all',
  	},
  	__(b)__ {
  		todoListByStatus: function() {
  
  		},
  	},
  	__(c)__ {
  		addTodo: function(__(d)__) {
  
  		},
  	},
  })
  ```

  `(a): Status`

  `(b): Mutations`

  `(c): Actions`

  `(d): todoListByStatus`