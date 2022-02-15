import sys
sys.stdin = open('1210_input.txt')

# 도착점과 연결되어있는 출발점을 찾자
for tc in range(1, 11):
    N = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 일단 값을 받아오자

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
        # 근데 아래의 경우는 finish_line_idx가 오른쪽 끝이거나 왼쪽 끝일 경우 조건을 확인하는 과정에서 인덱스 에러가 뜰 것임
        # 그래서 처음 배열 받아올 때 양 끝에 [0] 추가해줌
        if arr[end-1][finish_line_idx]==1 and arr[end][finish_line_idx-1]==1: # 위, 왼이 모두 1일때
            finish_line_idx += dj[0]
            arr[end][finish_line_idx] = 0
        elif arr[end-1][finish_line_idx]==1 and arr[end][finish_line_idx+1]==1: # 위, 오가 모두 1일때
            finish_line_idx += dj[2]
            arr[end][finish_line_idx] = 0
        elif arr[end-1][finish_line_idx]==1: # 위가 1일때
            end += di[1]
            arr[end][finish_line_idx] = 0
        elif arr[end][finish_line_idx-1]==1: # 왼이 1일때
            finish_line_idx += dj[0]
            arr[end][finish_line_idx] = 0
        elif arr[end][finish_line_idx+1]==1: # 오가 1일때
            finish_line_idx += dj[2]
            arr[end][finish_line_idx] = 0

    print(f'#{tc} {finish_line_idx-1}') # 앞에 [0] 하나를 추가해줬기 때문