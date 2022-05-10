# HomeWork
### Vanilla JavaScript

 JavaScript에서 표준(standard)가 중요한 이유를 서술하시오.

```javascript
// ans
// 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 되었다
// 그 결과 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생하게 됨. 그러한 이슈를 해소하기 위해 표준의 필요성이 대두되기 시작

// 크로스 브라우징이란?
// W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들괴, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론
```

```javascript
// 파편화 되어있는 브라우저들이 각자 다른 API를 제공했다
// 표준화가 재정된 이후 부터는 통일된 스크립트로도 대부분의 브라우저에서 정상저긍로 작동하게 되었다
```





### JavaScript T/F

아래의 설명을 읽고 T/F 여부를 작성하시오.

- DOM 에서 최상위 객체는 document다. `F` `최상위 객체는 window`
- getElementById 메서드보다 querySelector 메서드가 좋은 이유는 선택자를 더 유연하게 사용할 수 있기 때문이다. `T` `querySelector의 경우 id, class, 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 사용 가능`
- querySelectorAll 메서드를 통해 선택한 NodeList는 forEach 메서드를 사용할 수 있다. `T`
- document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다. `T`
- 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다 `F` `appendChild도 있었음` `append는 좀 더 관대함. 노드 객체 아니어도 추가 가능하며 한번에 여러개를 넣을 수 있음`