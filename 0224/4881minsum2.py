import sys
sys.stdin = open('4881_input.txt')

def backtracking(i, N, su_m, visited):
    global ans
    if i == N: # 다 돌았을 때
        if su_m < ans:
            ans = su_m
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                backtracking(i+1, N, su_m+num_list[i][j], visited)
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 100
    visited = [0]*N

    backtracking(0, N, 0, visited)
    print(f'#{tc} {ans}')