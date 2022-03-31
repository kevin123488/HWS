# 최소 생산 비용
# 첫 코드는 n**4의 복잡도를 가졌었다
# n**5였나? 아무튼
# 동철이 문제의 코드를 이용하여 풀 수 있을 것 같아 적용해보려 한다
import sys
sys.stdin = open('5209.txt')

def dfs(a, s, cnt): # 인덱스, 합계, cnt(몇개 더했는가)
    global sum
    if s > sum: # 구해둔 합계보다 연산중인 합계가 더 크다면        # 가지치기
        return
    if cnt == N+1: # N개 다 더했으면                          # 종료조건
        if s < sum: # 새로 구해준 값이 더 작으면
            sum = s # 값 바꿔주기
        return

    for i in range(N):                                      # 값 순회
        if visited[i] == 0: # 아직 방문하지 않았다면
            visited[i] = 1 # 방문표시 해주고
            dfs(a+1, s+arr[a][i], cnt+1) # 인덱스에 1 추가, s에는 해당하는 값 더하기
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    sum = 1000000000
    dfs(0, 0, 1) # 인덱스, 합, 횟수

    print(f'#{tc} {sum}')