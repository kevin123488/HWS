# 수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의
# 번호를 종이에 적어 제출
# 한 조에 제한 인원을 두지 않았기에, 한 사람이 여러장의 종이를 제출하거나
# 여러 사람이 한 사람을 지목한 경우 모두 같은 조
# 1~N까지의 출석번호, M장의 신청서
# 지목하지 않았으면서 지목당하지 않은 사람은 단독으로 조 구성

# 오답코드 + 시간초과

import sys
sys.stdin = open('5248.txt')

def dfs(a): # 현재 방문중인 번호
    global cnt
    visited[a] = 1 # 방문표시 해줌

    for i in range(1, len(ji_mok[a])): # a번호의 연결 정보에 대해
        if ji_mok[a][i] == 1 and visited[i] == 0: # 만약 a번호와 연결되어 있으면서 아직 방문하지 않은 곳 이라면?
            dfs(i)
            # visited[i] = 0
            # print(visited, i)

    # 더 돌 곳이 없으면?
    # 다음 번호로 넘어가자
    for k in range(len(arr)//2):
        if visited[arr[k*2]] == 0: # 아직 방문하지 않은 곳 이라면
            cnt += 1
            # print(f'thisisnew{arr[k*2]}')
            dfs(arr[k*2])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # arr에는 M쌍의 번호가 들어있음

    # 지목 정보를 담은 리스트를 만들어보자
    # 번호와 인덱스를 일치시켜 줘야 하므로
    ji_mok = [[0]*(N+1) for _ in range(N+1)]

    for i in range(len(arr)//2): # arr를 2칸씩 끊어서 활용할 예정
        ji_mok[arr[i*2]][arr[i*2+1]] = 1 # 지목 및 연결 정보
        ji_mok[arr[i*2+1]][arr[i*2]] = 1
        # 무향성? 유향성?
        # 무향성으로 하자

    visited = [0]*(N+1)
    # visited에 방문표시를 하며 탐색해보자
    # 일단 시작점은 arr[0]
    # 그 지점에서 시작하여 연결되어있는 모든 번호를 visited에 저장한다
    # 탐색이 완료되면 그 다음 번호이면서 방문하지 않은 번호를 찾는다
    # 거기서 다시 시작한다 (다시 시작할 때 cnt + 1 해주자, cnt 초기값은 1)
    # 다 되고 난 후 visited의 0 개수를 세어 그 값 -1을 cnt에 더해준다
    cnt = 1
    dfs(arr[0])
    ans = visited.count(0) - 1 + cnt
    print(f'#{tc} {ans}')