# tc 6에서 걸림
# 시간초과

import sys
sys.stdin = open('5250.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j, cnt, h):
    global ans
    visited[i][j] = 1 # 방문표시를 해주자
    if cnt > ans:
        return
    if i == N-1 and j == N-1: # 도착점에 도달?
        if ans > cnt:
            ans = cnt
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] < ans-1: # 만약 이동할 좌표가 범위 내에 있으면서 방문하지 않은 곳 이라면?
            if arr[ni][nj] > h:
                dfs(ni, nj, cnt+1+arr[ni][nj]-h, arr[ni][nj])
            else:
                dfs(ni, nj, cnt+1, arr[ni][nj])
            visited[ni][nj] = 0 # 여러 케이스중 최적의 해를 찾아야 하므로

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 출발지는 [0][0], 도착지는 [N-1][N-1]
    # 이동시 연료 1만큼 필요
    # 거기에 추가적으로 더 높은 칸으로 이동하는 경우 그만큼의 연료가 더 필요

    visited = [[0]*N for _ in range(N)]
    ans = 1000000
    dfs(0, 0, 0, arr[0][0]) # 현재 좌표의 i, j, 연료량, 현재 높이

    print(f'#{tc} {ans}')