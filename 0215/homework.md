## Homework

**SWEA 1210번 문제**

도착점과 연결되어있는 출발점의 좌표를 구하는 문제

```python
import sys
sys.stdin = open('1210_input.txt')

# 도착점과 연결되어있는 출발점을 찾자
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 일단 값을 받아오자

    # 도착점에서 거슬러 올라가며 arr[0]에 있는 값과 만날 경우를 생각해보자
    # 도착점은? arr[99]를 순회하다 2인값이 있다면 그 값의 인덱스를 뽑아내면 된다

    finish_line_idx = 0
    for idx, i in enumerate(arr[99]):
        if i == 2:
            finish_line_idx += idx

    end = 99
    finish_line = arr[end][finish_line_idx]
    di = [0, -1, 0] # 왼, 위, 오 순으로
    dj = [-1, 0, 1] # 왼, 위, 오 순으로

    # finish_line에서 주변을 조회해보자. 위, 왼 모두 1이면 왼쪽으로 -> finish_line_idx에 dj[0] 더해주자
    # 위, 오 모두 1이면 오른쪽으로 -> finish_line_idx에 dj[2] 더해주자
    # 위만 1이면 위쪽으로 -> end값에 di[1] 더해주자
    # 지나온 길의 값은 0으로 바꿔주어야 되돌아가지 않음
    
    while end > 0: # 첫 줄에 도달할 때 까지
        if arr[end-1][finish_line_idx]==1 and arr[end][finish_line_idx-1]==1:
            finish_line_idx += dj[0]
            arr[end][finish_line_idx] = 0
        elif arr[end-1][finish_line_idx]==1 and arr[end][finish_line_idx+1]==1:
            finish_line_idx += dj[2]
            arr[end][finish_line_idx] = 0
        elif arr[end-1][finish_line_idx]==1:
            end += di[1]
            arr[end][finish_line_idx] = 0
        elif arr[end][finish_line_idx-1]==1:
            finish_line_idx += dj[0]
            arr[end][finish_line_idx] = 0
        elif arr[end][finish_line_idx+1]==1:
            finish_line_idx += dj[2]
            arr[end][finish_line_idx] = 0

    print(f'#{tc} {finish_line_idx}')
```

중간에 인덱스 에러가 뜬다. 난감하다... 자야하는데

+

확인해보니 해당 좌표가 오른쪽 끝 지점으로 갔을 때 finish_line_idx + 1을 조회하는 과정에서 오류가 발생하는 것 같다.

end의 경우 범위가 잘 조절되어있으니 ㄱㅊ. 문제는 finish_line_idx 인데... 어떻게 범위를 잡아줘야 할까?