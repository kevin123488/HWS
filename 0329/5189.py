# 전자 카트
import sys
sys.stdin = open('input_5189.txt')

def dfs(s, ans): # 출발노드 s와 ans
    # global min_ans
    visited[s] = 1 # 방문체크를 하여 들른 곳은 다시 들르지 않도록 하자
    if visited.count(0) == 1: # 방문처리가 다 되어 visited[0]을 제외한 곳에 1이 들어가있다면
        ans += arr[s-1][0]
        # if min_ans > ans: # 처음 설정해준 min_ans와 비교하여 구해준 ans가 더 적다면?
        #     min_ans = ans # 구해준 ans를 min_ans 자리에 넣어주자
        #     ans_list.append(ans)
        ans_list.append(ans)
        return
    # 다음 방문지를 찾아야 한다. 방문지의 노드는 1부터 N까지.
    for i in range(1, N+1):
        if visited[i] == 0: # 만약 방문하지 않은 노드라면?
            dfs(i, ans + arr[s-1][i-1])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # N*N의 리스트를 받음

    # 1에서 출발, 모든 구역을 돌고 난 후 다시 1로 돌아가야됨
    # 방문체크 필요

    visited = [0]*(N+1) # 노드의 번호와 인덱스를 맞춰주기 위함
    # 1->2 일때 arr[0][1]의 값을 추가해줘야 함. a->b로 이동할 때 arr[a-1][b-1]의 값을 추가해줘야 함.
    # min_ans = 10200
    ans_list = []
    # min_ans와 비교하며 값이 더 적다면 담아주고, 크다면 거기서 return을 하자
    dfs(1, 0) # 출발노드 1과 ans를 인자로 넣어주자
    print(f'#{tc} {min(ans_list)}')