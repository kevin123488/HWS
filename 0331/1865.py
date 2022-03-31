# N명의 직원
# 해야할 일 N개
# 직원이 어떤 일을 성공할 확률이 arr를 통해 받아짐
# 주어진 일이 모두 성공할 확률을 최대로 하는 경우의 확률을 출력하자
# 직원에겐 해야 할 일을 하나씩만 배분한다

import sys
sys.stdin = open('1865.txt')

def dfs(a, b, cnt): # 인덱스, 성공확률, cnt(몇개 곱했는가)
    global hwak
    if b <= hwak:
        return # 곱하는 중인 것이 이미 구해둔 확률보다 낮을 경우 더 볼 것 없음
    if cnt == N+1: # N개 다 곱했으면
        if b > hwak: # 이번에 구한 값이 이전 값보다 크면
            hwak = b # hwak에 이번에 구한 값 넣어주기
        return
    # if b == 0: # 확률이 0?
    #     return # return

    for i in range(N): # 방문표시를 확인할 예정
        if visited[i] == 0: # 아직 방문하지 않은 곳 이라면
            visited[i] = 1 # 방문표시 해주고
            dfs(a+1, b*(arr[a][i]/100), cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 일을 성공할 확률을 담아둔 리스트
    # arr[0][1]이면 0번째 사람이 1번째 일을 성공할 확률
    # 모두 성공할 확률 -> 곱해가며 연산. 값/100을 계속해서 곱해주자

    visited = [0]*(N)
    hwak = 0
    dfs(0, 1, 1)
    ans = '{:.6f}'.format(hwak*100)
    print(f'#{tc} {ans}')