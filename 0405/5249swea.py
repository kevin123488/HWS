# 최소 신장 트리
# 오답 코드 + 시간초과
import sys
sys.stdin = open('5249.txt')

def dfs(a, cnt): # 조회중인 노드와 가중치의 합을 받아오자
    global ans
    visited[a] = 1 # 조회중인 노드 방문표시 해주고
    if cnt > ans:
        return
    if visited.count(0) == 0: # 모든 노드에 방문해서 방문기록에 0이 없다면
        if ans > cnt:
            ans = cnt
        return
    for i in range(len(injeup[a])): # 방문중인 노드와 연결되어있는 지점을 골라서
        if injeup[a][i] != 0 and visited[i] == 0: # a와 연결되어 있으면서 방문기록은 없는 노드라면?
            dfs(i, cnt+injeup[a][i]) # i에 대해서 다시 탐색, 그 연결선의 거리에 맞는 값을 더해주자
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드번호, E: 간선개수
    arr = [list(map(int, input().split())) for _ in range(E)]
    # [[시작노드, 끝노드, 가중치], [n1, n2, w],..., [n1, n2, w]]

    # 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할
    # 때, 가중치의 합이 최소가 되도록 하는 트리를
    # 최소신장트리 라고 함
    # 0~V까지의 노드와 E개의 간선을 가진 그래프가 주어진다
    # 최소신장트리를 구성하는 간선의 가중치를 모두 더하자

    # 인접행렬을 구하자
    injeup = [[0]*(V+1) for _ in range(V+1)]
    for i in arr: # arr 순회하면서
        injeup[i[0]][i[1]] = i[2]
        injeup[i[1]][i[0]] = i[2]

    ans_list = []
    ans = 100000000
    # 시작지점을 모든 노드로 잡아보자
    for i in range(V+1):
        visited = [0] * (V + 1)
        dfs(i, 0)
        ans_list.append(ans)

    print(f'#{tc} {min(ans_list)}')