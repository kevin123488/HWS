import sys
sys.stdin = open('1249.txt')

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b, cnt): # 순회중인 좌표와 cnt값을 넣어주자
    global ans
    visited[a][b] = 1
    if cnt > ans:
        return
    if a == N-1 and b == N-1:
        if ans > cnt:
            ans = cnt
        return

    for i in range(4): # 탐색 시작
        ni = a + di[i]
        nj = b + dj[i]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            dfs(ni, nj, cnt+arr[ni][nj])
            visited[ni][nj] = 0 # 모든 경우를 돌아줘야 하므로 visited의 초기화가 필요하다

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 배열엔 파여진 도로의 깊이가 주어진다
    # 도달한 칸의 깊이만큼 복구 시간이 걸린다
    # 출발지: [0][0], 도착지[N-1][N-1]
    # 이동하는 시간보다 복구하는데 걸리는 시간이 월등히 높다
    # 그러므로 배열 칸의 합이 최소가 되는 경우를 구하면 됨
    # dfs를 이용하여 모든 경우의 수를 체크, 도중 가지치기를 통해 백트래킹

    # 방문체크를 해줄 리스트를 만들자
    visited = [[0]*N for _ in range(N)]

    ans = 1000000
    dfs(0, 0, 0) # 탐색 시작지점이 [0][0] 이므로
    print(f'#{tc} {ans}')