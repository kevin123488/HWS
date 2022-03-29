# 최소 합
import sys
sys.stdin = open('input_5188.txt')

# 델타탐색
di = [0, 1] # 오른쪽, 아랫쪽
dj = [1, 0] # 오른쪽, 아랫쪽

def dfs(a, b, c): # a: 탐색중인 좌표의 행 값, b: 탐새중인 좌표의 열 값, c: 누적된 ans
    global min_ans
    c += arr[a][b]
    if c >= min_ans:
        return
    if a == N-1 and b == N-1: # 만약 arr[N-1][N-1]에 도착했다면
        if c < min_ans:
            min_ans = c
            ans_list.append(c)
        return
    for i in range(2):
        ni = a + di[i]
        nj = b + dj[i]
        if 0<=ni<N and 0<=nj<N: # 범위 내에만 있으면 이동이 가능함
            dfs(ni, nj, c)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # N*N의 배열을 받음

    # arr[0][0] 에서 출발해 arr[N-1][N-1]에 도달할 때 까지 거치는 값들의 합이 최소가 되게 하라(탐색시 오른쪽, 그리고 아랫쪽으로만 이동 가능)
    # 오른쪽과 아랫쪽으로만 이동 가능하므로, visited 만들어줄 필요 없음
    min_ans = 1000000
    ans_list = [] # 탐색이 한번 끝날때마다 여기 값을 더해줄 예정
    dfs(0, 0, 0)
    print(f'#{tc} {ans_list[-1]}')