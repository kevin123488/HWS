import sys
from collections import deque
sys.stdin = open('1249.txt')

# 델타탐색
di = [0, 1] # 우, 하만 신경쓰자
dj = [1, 0] # 우, 하만 신경쓰자

def bfs(a, b, cnt):
    global ans
    que = deque()
    que.append((a, b, cnt))
    while que:
        x, y, z = que.popleft()
        visited[x][y] = 1
        if z > ans:
            continue
        if x == N-1 and y == N-1:
            if ans > z:
                ans = z
            continue

        for i in range(2):
            ni = x + di[i]
            nj = y + dj[i]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                que.append((ni, nj, z+arr[ni][nj]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    ans = 10000000
    bfs(0, 0, 0)
    print(f'#{tc} {ans}')