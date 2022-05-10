# bfs를 이용하여 풀어보자
# tc 5번에서 런타임 에러
import sys
from collections import deque
sys.stdin = open('5250.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j, cnt, h):
    global ans
    que = deque()
    que.append((i, j, cnt, h))
    while que:
        i, j, cnt, h = que.popleft()
        if cnt > ans:
            continue
        if i == N-1 and j == N-1:
            if ans > cnt:
                ans = cnt
            continue

        for z in range(4):
            ni = i + di[z]
            nj = j + dj[z]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                if visited[ni][nj] > visited[i][j] + 1 + (arr[ni][nj] - h):
                    visited[ni][nj] = visited[i][j] + 1 + (arr[ni][nj] - h)
                    que.append((ni, nj, cnt + 1 + arr[ni][nj] - h, arr[ni][nj]))
                else:
                    que.append((ni, nj, cnt+1, arr[ni][nj]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[999999999] * N for _ in range(N)]
    ans = 10000000
    bfs(0, 0, 0, arr[0][0])  # 현재 좌표의 i, j, 연료량, 현재 높이

    print(f'#{tc} {ans}')