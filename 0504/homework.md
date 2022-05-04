## 0504 HW

1. **아래의 설명을 읽고 T/F 여부를 작성하시오.**

   • SPA는 Single Pattern Application의 약자이다. `F` `single page application`

   • SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 
   이후부터는 페이지 갱신에 필요한 데이터만 전달받는다. `T`

   • Vue.js에서 말하는 ‘반응형’은 데이터가 변경되면 이에 반응하여,
   연결된 DOM이 업데이트되는 것을 의미한다. `T`

   • 동일한 요소에 v-for와 v-if 두 디렉티브가 함께 작성된 경우, 
   매 반복 시에 v-if의 조건문으로 요소의 렌더링 여부를 결정한다. ``

   • v-bind 디렉티브는 “@“, v-on 디렉티브는 “:” shortcut(약어)을 제공한다. `F` `v-bind는 :, v-on은 @을 이용`

   • v-model 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터
   바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다. `F` `양방향 바인딩을 이룸`



2. **MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오**

   `ans: Model View ViewModel`

   `Model: Vue에서의 Model은 Javascript Object이다. Vue Instance 내에서 data라는 이름으로 존재. 이 data가 바뀌면? view(dom)가 반응함`

   `View: Vue에서의 View는 DOM을 의미함. --> Data의 변화에 따라 바뀌는 대상`

   `ViewModel: Vue에서의 ViewModel은 모든 Vue Instance를 의미한다. View(DOM)과 Model(data) 사이에서 그와 관련된 일을 처리함`



3. **다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오**

   ```html
   <div id="app">
       {{ (a) }}
   </div>
   
   <script>
   	const app = (b) ({
           el: (c),
           data: {
               message: 'Hello, World!',
           },
       })
   </script>
   ```

   `ans`

   `(a): message`

   `(b): new Vue`

   `(c): '#app'`