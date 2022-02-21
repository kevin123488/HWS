## Homework

SWEA 2005번 문제-파스칼 삼각형 만들기

```python
# 크기가 N인 파스칼의 삼각형을 만들자
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    memo = [[0]*(N) for _ in range(N)] # memo를 만들자
    # 위의 memo에 값들을 추가해주자
    for i in range(N):
        for j in range(N):
            if j == 0:
                memo[i][j] += 1
            elif i>0 and j>0:
                memo[i][j] += (memo[i-1][j-1] + memo[i-1][j])

    ans_list = []
    for k in range(N):
        ans = memo[k][:k+1]
        ans_list += [ans]

    print(f'#{tc}')

    for z in ans_list:
        for x in z:
            print (x, end=' ')
        print()
```

로직

1. 0으로 가득 찬 2차원 리스트를 만들자
2. 그 리스트의 0 값들을 조건에 맞게 채워주자
   - j가 0의 인덱스를 가지는 경우 -> memo`[i][j]` = 1
   - i와 j의 값이 0보다 클 경우 -> memo`[i][j]` = memo`[i-1][j-1]`+memo`[i-1][j]`

위의 방식을 이용해 2차원 리스트 memo를 파스칼 삼각형 + 빈공간 0으로 만드는데 성공

3. i 인덱스에 따라 해당 행을 슬라이싱 해 필요한 부분만을 get
4. 그걸 또다른 리스트에 넣어 또다른 이차원리스트(필요한 부분만 있는)를 만든다
5. 포문과 print를 적절히 이용하여 요구하는 형태에 맞게 출력