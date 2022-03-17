## 0317 HW

```python
for tc in range(1, 11):
    N = int(input()) # 정점의 총 수
    tree = [0]
    for i in range(N):
        arr = list(input().split())
        tree.append(arr[1])

    # tree에 값을 넣어뒀음
    # 역으로 조회하면서 계산해보자
    k = N
    while k > 1:
        if tree[k//2] == '+':
            tree[k//2] = int(tree[(k//2)*2]) + int(tree[(k//2)*2+1])
        elif tree[k//2] == '-':
            tree[k//2] = int(tree[(k//2)*2]) - int(tree[(k//2)*2+1])
        elif tree[k // 2] == '*':
            tree[k//2] = int(tree[(k//2)*2]) * int(tree[(k//2)*2+1])
        elif tree[k // 2] == '/':
            tree[k//2] = int(tree[(k//2)*2]) / int(tree[(k//2)*2+1])
        else:
            k -= 1

    ans = round(tree[1])
    print(f'#{tc} {ans}')
```

테스트케이스 4개까지만 돌고 5개째부턴 에러가 뜬다.

왜 그런가 했더니,,,,

결론부터 말하자면, 문제를 너무 간단하게 봐서 그렇다.

완전이진트리라고 생각하고 문제를 풀었는데, 에러가 뜨고 난 후 찬찬히 다시 문제를 읽어보니 그냥 이진트리였다. 그래서 저기 while > if, elif문에서 계속 valueerror가 떴던 것 이었다...

내일 다시 풀어봐야지