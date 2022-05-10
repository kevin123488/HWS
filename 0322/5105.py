# 미로의 거리
# N*N 미로에서 출발지와 목적지가 주어짐
# 최소 몇 개의 칸을 지나면 출발지에서 목적지에 도달할 수 있는지 구하시오
# 0-> 통로, 1-> 벽, 2-> 출발지점, 3-> 도착지점

import sys
sys.stdin = open('5105.txt')

# 델타탐색
di = [0, 1, 0, -1] # 우하좌상
dj = [1, 0, -1, 0] # 우하좌상

def bfs(x, y, cnt):
    que = []
    que.append([x, y, cnt])
    while que:
        [x, y, cnt] = que.pop(0)
        for i in range(4): # 델타탐색
            ni = x + di[i]
            nj = y + dj[i]
            if 0<= ni <N and 0 <= nj < N: # arr의 법위 내일 경우
                if arr[ni][nj] == 0: # 조회할 칸이 통로라면?
                    arr[ni][nj] = 1 # 방문 표시해두고
                    que.append([ni, nj, cnt+1]) # 해당하는 좌표를 que에 넣어줌
                if ni == z and nj == w:
                    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = int(arr[i][j])
            if arr[i][j] == 2: # 출발점
                x, y = i, j
            if arr[i][j] == 3: # 도착점
                z, w = i, j

    ans = bfs(x, y, 0)
    if ans == None:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {ans}')