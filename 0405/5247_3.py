from collections import deque

def bfs(a):
    que = deque()
    que.append((a, 0))
    while que:
        pass

T = int(input())
for tc in range(T+1):
    N, M = map(int, input().split())
    bfs(N)