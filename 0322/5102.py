# 노드의 거리

# v: 노드개수
# E: 간선 정보의 개수
import sys
sys.stdin = open('5102.txt')

def bfs(S):
    que = []
    que.append(S)
    visited[S] = 1 # 방문표시
    while que:
        S = que.pop(0)
        for i in range(V+1):
            if find_arr[S][i] == 1 and visited[i] == 0: # 현재 있는 노드와 연결이 되어있으면서 방문하지 않은 곳
                que.append(i) # 그 연결된 노드를 que에 넣어준다
                visited[i] = visited[S] + 1 # 한칸 이동했으니 그만큼 올라감
                if i == G:
                    return visited[G]

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V는 노드의 개수, E는 간선 정보의 개수
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선의 정보가 들어있는 리스트
    S, G = map(int, input().split()) # S는 출발노드, G는 도착노드

    # 인접행렬을 만들자
    find_arr = [[0]*(V+1) for __ in range(V+1)] # (V+1)^2인 행렬을 만들어 둠
    for i in range(V+1): # 노드의 번호와 인덱스를 맞춰주기 위함
        for j in range(V+1): # 마찬가지
            if [i, j] in arr:
                find_arr[i][j] = 1
                find_arr[j][i] = 1

    visited = [0]*(V+1) # 방문 정보를 기록할 리스트
    ans = bfs(S) - 1 # 시작지점에서 이미 1을 갖고 있었으므로(1부터 더해주기 시작하였으므로)
    print(f'#{tc} {ans}')