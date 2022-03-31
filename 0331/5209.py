# 최소 생산 비용
# 봄부터 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩
# 생산하려 한다.

# 테스트케이스 3개까지 돌고 끝나는 시간초과 코드
# 생각해보니 열만 조회하고, 행은 1씩 증가시키는 방식으로 해도 괜찮을 듯 싶다
# 그렇게 되면 함수에서의 이중포문이 그냥 포문으로, 함수 밖에서의 이중포문도 그냥 포문으로 바꿀 수 있을 것
# 4중포문 -> 이중포문
import sys
sys.stdin = open('5209.txt')

def find_ans(a, b, ans, cnt): # 조회중인 인덱스, 합, 더한 횟수
    global real_ans

    if ans > real_ans: # 더하는중인 ans의 값이 기존에 구해둔 real_ans보다 크면?
        return # return

    madeby[a] = 1 # 해당 공장에 방문표시
    obj[b] = 1 # 해당 제품에 방문표시
    if cnt == N: # N개의 제품을 모두 생산
        if real_ans > ans:
            real_ans = ans
        return
    else: # 아직 다 생산하지 않았다면
        for i in range(len(madeby)):
            for j in range(len(obj)):
                if madeby[i] == 0 and obj[j] == 0: # 제품도, 공장도 아직 방문하지 않은 곳 이라면?
                    find_ans(i, j, ans+arr[i][j], cnt+1) # 그 지점 방문해라
                    madeby[i] = 0 # 방문하고 난 뒤엔 다시 비워주자
                    obj[j] = 0 # 방문하고 난 뒤엔 다시 비워주자

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # A, B, C ...  공장, 1, 2, 3 ... 제품
    # 한 곳당 한 가지씩만 생산 가능, 모든 곳에서 1개씩의 제품을 생산해야 함
    # 즉 모든 요소의 [i, j]가 겹치지 않아야 한다
    # arr[0][0]에서 순회를 시작할 것
    # madeby = [0]*(N) # 공장
    # obj = [0]*(N) # 제품

    real_ans = 100000000
    for i in range(N):
        for j in range(N):
            madeby = [0] * (N)  # 공장
            obj = [0] * (N)  # 제품
            find_ans(i, j, arr[i][j], 1)

    print(f'#{tc} {real_ans}')