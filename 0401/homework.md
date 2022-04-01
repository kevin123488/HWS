## 0401 HW

swea 5247 연산

```python
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
```

길이 100만쯤 되는 리스트를 만들 생각을 하지 못했다는 점, 방문 체크를 통해 지나는 값들의 중복을 제거해 줄 생각을 못했다는 점이 이 문제를 오래 걸리게 한 요인이 아닐까 싶다...



+



처음엔 dfs로 풀었었는데, tc 3번부터 막혀서 bfs로 다시 짰다!