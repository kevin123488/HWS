import sys
sys.stdin = open('4875.txt')

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1]+list(map(int, input()))+[1] for _ in range(N)] # (N+2)*(N+2)의 2차원 리스트를 받아옴
    arr = [[1]*(N+2)] + arr + [[1]*(N+2)]