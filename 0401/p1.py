'''
입력값
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# dfs
def dfs(a): # 현재 지점을 담아줌
    visited[a] = 1 # 방문표시
    print(a)
    if visited.count(0) == 1:
        return
    for i in range(len(injeup[a])):
        if injeup[a][i] == 1 and visited[i] == 0: # a와 연결되어 있는 노드일 경우
            dfs(i)

arr = list(map(int, input().split()))
N = max(arr)
injeup = [[0]*(N+1) for _ in range(N+1)] # 노드의 번호와 인덱스를 일치시켜주기 위함
# 해당 정보를 인접행렬로 만들어주면?
for i in range(len(arr)//2):
    injeup[arr[i*2]][arr[i*2+1]] = 1
    injeup[arr[i*2+1]][arr[i*2]] = 1

# 연결정보를 1로 표시해줌
visited = [0]*(N+1)
dfs(1)