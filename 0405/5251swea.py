# 최소 이동거리
# A 도시에는 E개의 일방통행 도로 구간이 있다
# 각 구간이 만나는 연결지점은 0번부터 N번까지의 번호가 붙어있다
# 구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때 0번 지점에서 N번 지점까지
# 이동하는데 걸리는 최소한의 거리가 얼마인지 출력
# 모든 연결지점을 거칠 필요는 없다
import sys
sys.stdin = open('5251.txt')

def dfs(a, b): # 순회중인 노드와 이동거리의 합계를 입력
    global ans
    if b > ans:
        return
    if a == N: # 끝번호와 일치하는 순간
        if ans > b:
            ans = b
        return
    for i in range(len(injeup[a])): # 순회중인 노드의 연결정보를 조회
        if injeup[a][i] != 0 and visited[i] == 0:
            visited[i] = 1 # 방문표시 해주고
            dfs(i, b+injeup[a][i][1]) # i번 노드에 대해 다시 탐색
            visited[i] = 0 # 여러 경우의 수중 가장 짧은 거리를 찾아야 하므로


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    # 인접행렬을 만들어보자
    injeup = [[0]*(N+1) for _ in range(N+1)] # 0부터 N까지의 연결 정보를 담을 예정
    for i in arr:
        injeup[i[0]][i[1]] = [1, i[2]] # 연결 유무, 연결 거리를 넣어두자
    
    # 인접행렬을 순회하자
    ans = 1000000000000
    visited = [1] + [0] * N # 0번 노드부터 N번 노드까지 입력
    dfs(0, 0) # 탐색은 0번부터 시작

    print(f'#{tc} {ans}')