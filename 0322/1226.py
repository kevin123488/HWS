# 미로1

# swea 1226번 문제
# 미로탐색
import sys
sys.stdin = open('1226.txt')

# 2차원 리스트를 받음
# 1-> 벽, 2-> 출발점, 3-> 도착점, 0-> 통로
# 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하라

# 델타탐색
di = [0, 1, 0, -1] # 우하좌상
dj = [1, 0, -1, 0] # 우하좌상

def bfs(i, j):
    que = []
    que.append([i, j])
    while que:
        [i, j] = que.pop(0)
        for k in range(4): # 델타탐색 시작
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<16 and 0<=nj<16:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    que.append([ni, nj])
                if arr[ni][nj] == 3:
                    return 1
    return 0

for tc in range(1, 11):
    num = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                ans = bfs(i, j)

    print(f'#{tc} {ans}')