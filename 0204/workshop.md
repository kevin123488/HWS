# WorkShop

### Semantic Tag

제시된 semantic.html과 semantic.css를 수정하여 다음 이미지와 같은 형태가 되도록 코드를 작성하시오



**html 코드**

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="b-black br-4 bgc-lightgray m-4 p-4 ta-center">
    <h1>header</h1>
  </header>
  <nav class="b-black br-4 bgc-lightgray m-4 p-4">
    <h2>nav</h2>
  </nav>
  <div class="clearfix">
    <section class="p-4 b-black br-4 bgc-lightgray section">
      <h2>section</h2>
      <article class="p-4 b-black br-4 bgc-white">
        <h3>article1</h3>
      </article>
      <article class="p-4 b-black br-4 bgc-white">
        <h3>article2</h3>
      </article>
    </section>
    <aside class="p-4 b-black br-4 bgc-lightgray aside">
      <h2>aside</h2>
    </aside>
  </div>  
  <footer class="b-black br-4 bgc-lightgray m-4 p-4">
    <h2>footer</h2>
  </footer>
</body>
</html>
```



**CSS 코드**

```css
/* 아래 코드는 수정하지 마세요. */
body {
  font-family: Arial;
  width: 800px;
}

section {
  float: left;
  margin-left: 4px;
}

aside { 
  /* position: absolute;
  bottom: 305px;
  left: 510px; */
  float: right;
  margin-right: 4px;
}

.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

/* 여기서부터 작성하세요. */
/* 모든 스타일 요소를 ***클래스***로 만들어 작성 후 사용합니다. */

/* 1. article 태그는 white로 나머지 
시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */

.bgc-white {
  background-color: white;
}

.bgc-lightgray {
  background-color: lightgray
}
/* 2. header, nav, footer 태그의 
margin을 4px로 만들어주세요. */
.m-4 {
  margin: 4px;
}

/* 3. header, nav, footer 태그의 
padding을 4px로 만들어주세요. */
.p-4 {
  padding: 4px;
}

/* 4. h1 태그를 수평 중앙 정렬 시켜주세요. */
.ta-center {
  text-align: center;
}

/* 5. section 태그는 width 490px height 300px, 
   aside 태그는 width 280px height 300px로 만들어주세요.*/

.section {
  width: 490px;
  height: 300px;
}

.aside {
  width: 280px;
  height: 300px;
}

/* 6. 모든 semantic 태그의 border 
두께를 1px, 실선, 검은색으로 만들어주세요. */
.b-black {
  border: 1px solid black
}

/* 7. 모든 semantic 태그의 
border 모서리 반경을 4px로 만들어주세요. */
.br-4 {
  border-radius: 4px;
}
```

