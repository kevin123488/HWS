## 0426 WS

```javascript
// 내 답변

function deepCopy(arr) {
      let a = []
      for (let b of arr) {
        a.push(b)
      }
      return a
    }

function isPalindrome(str) {
    let ans = []
    for (let a of str.split('')) {
        if (a!==' ') {
            ans.push(a)
        }
    }
    reverseAns = deepCopy(ans).reverse().join('') // .join 해주는 이유는? 리스트끼리 비교할땐 참조중인 곳을 기준으로 비교하기 때문에, 단순히 속해있는 요소들의 값이 같다고 해서 비교값이 true가 되지는 않기 때문
    ans = ans.join('')
    if (ans === reverseAns) {
        return true
    } else {
        return false
    }
}
```



```javascript
// 교수님 답변

function isPalindrome(str) {
    const trimStr = str.replaceAll(' ', '')
    const arr = trimStr.split('')
    arr.reverse()
    const reversedStr = arr.join('')
    return trimStr === reversedStr
}
```

