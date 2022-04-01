# dfs 이용(시간초과)
# 연산
# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려 한다
# 사용 가능 연산은 +1, -1, *2, -10
# 최소 몇 번의 연산이 필요한가?
# 연산의 중간결과는 항상 백만 이하의 결과여야 함
# N=2, M=7인 경우, (2+1)*2+1로 3번의 연산이 필요

import sys
sys.stdin = open('5247.txt')

def dfs(a, b, cnt): # a는 연산대상, b는 목표값, cnt는 연산횟수
    global ans
    visited[a] = 1
    if a == b: # 목표값에 도달했으면
        if ans > cnt: # 기존의 값보다 이번에 구한 값이 더 적을 경우
            ans = cnt # ans 값을 당시의 cnt로 바꿔주자
        return
    if cnt > ans: # 카운트중인 연산 횟수가 기존의 값보다 크다면 더 볼 것 없음
        return
    if 0<a+1<=1000000 and visited[a-10] == 0:
        dfs(a+1, b, cnt+1)
        visited[a+1] = 0
    if 0<a-1<=1000000 and visited[a-10] == 0:
        dfs(a-1, b, cnt+1)
        visited[a-1] = 0
    if 0<a*2<=1000000 and visited[a-10] == 0:
        dfs(a*2, b, cnt+1)
        visited[a*2] = 0
    if 0<a-10<=1000000 and visited[a-10] == 0:
        dfs(a-10, b, cnt+1)
        visited[a-10] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ans = 1000000
    visited = [0]*1000001
    dfs(N, M, 0)
    print(f'#{tc} {ans}')