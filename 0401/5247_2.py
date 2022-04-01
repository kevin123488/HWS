from collections import deque
import sys
sys.stdin = open('5247.txt')

def bfs(a, cnt): # 연산대상, 목표, 카운트 횟수
    global ans
    que = deque()
    que += [(a, cnt)]
    visited = [0]*1000050
    while que:
        x, y = que.popleft()
        if x == M:
            if ans > y:
                ans = y
            continue
        if y > ans:
            continue
        if 0< x+1 <= 1000000 and visited[x+1] == 0:
            que.append((x+1, y+1))
            visited[x+1] = 1
        if 0< x-1 <= 1000000 and visited[x-1] == 0:
            que.append((x-1, y+1))
            visited[x-1] = 1
        if 0< x*2 <= 1000000 and visited[x*2] == 0:
            que.append((x*2, y+1))
            visited[x*2] = 1
        if 0< x-10 <= 1000000 and visited[x-10] == 0:
            que.append((x-10, y+1))
            visited[x-10] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 1000000
    bfs(N, 0)
    print(f'#{tc} {ans}')