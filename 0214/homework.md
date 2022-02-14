## swea 1209번 문제



오늘 배운 행 우선, 열 우선 순회를 사용해볼 수 있는 기본적인 문제였다.

```python
import sys
sys.stdin = open('1209_input.txt')

def my_max(args):
    for i in range(len(args)-1):
        if args[i] > args[i+1]:
            args[i], args[i+1] = args[i+1], args[i]
    return args[-1]

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행 우선 순회로 각 행의 sum을 구하자
    # 열 우선 순회로 각 열의 sum을 구하자
    # 대각선 2개의 합을 구하자
    # 각 행의 합, 열의 합, 대각선들의 합을 하나의 리스트에 담아 버블정렬을 이용해 가장 큰 값을 구해주자

    # 행 우선 순회
    the_real_sum_list = [] # 각 행, 열, 대각선의 합을 넣어줄 리스트. 나중에 정렬해서 가장 큰 값 구할때 쓸 것
    for i in range(100): # 0부터 99까지의 인덱스
        sum_list = 0 # 행의 합. 행이 바뀔때마다 값을 초기화 해야하므로 여기 둠
        for j in range(100): # 0부터 99까지의 인덱스
            sum_list += arr[i][j]
        the_real_sum_list += [sum_list] # 각 행들의 합이 들어갈 것

    for j in range(100):
        sum_list_2 = 0
        for i in range(100):
            sum_list_2 += arr[i][j]
        the_real_sum_list += [sum_list_2] # 각 열들의 합이 들어갈 것

    sum_list_3 = 0
    for k in range(100):
        sum_list_3 += arr[k][k]
    the_real_sum_list += [sum_list_3] # 대각선 1개의 합이 들어갈 것

    sum_list_4 = 0
    for z in range(100):
        sum_list_4 += arr[z][99-z]
    the_real_sum_list += [sum_list_4] # 나머지 대각선 1개의 합이 들어갈 것

    ans = my_max(the_real_sum_list)
    print(f'#{tc} {ans}')
```

금, 토, 일동안 웹공부만 하다보니 뭔가 버벅대는 느낌이었다. 다시 열심히 해야지...