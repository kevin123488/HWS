# 스도쿠 조건 만족 -> 1 출력
# 스도쿠 조건 만족ㄴ -> 0 출력
# 스도쿠 조건: 가로줄, 세로줄, 3*3 네모 안에 각각 1~9까지 하나씩 들어있어야 함
import sys
sys.stdin = open('스도쿠_input.txt')
# 리스트 내의 9개 요소가 1부터 9까지의 숫자로, 각각 1개씩 들어있는지 아닌지 확인하는 함수
def isittrue(args):
    if len(set(args)) == 9:
        return True
    else:
        return False

# 사각범위를 판정하는 함수
def sa_gak_true(arr, a, b):
    sa_gak = []
    cnt_sa = 0
    for i in range(9):
        for j in range(9):
            if 0+a <= i <= 2+a and 0+b <= j <= 2+b:
                sa_gak += [arr[i][j]]
                if len(sa_gak) == 9:
                    if isittrue(sa_gak):
                        sa_gak = []
                    else:
                        cnt_sa += 1
                        sa_gak = []
    if cnt_sa == 0:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행부터 만족하는지 확인해보자
    ga_ro = []
    cnt = 0
    for i in range(9):
        for j in range(9):
            ga_ro += [arr[i][j]]
        if len(ga_ro) == 9:
            if isittrue(ga_ro):
                ga_ro = []
            else:
                cnt += 1
                ga_ro = []

    se_ro = []
    for ii in range(9):
        for jj in range(9):
            se_ro += [arr[jj][ii]]
        if len(se_ro) == 9:
            if isittrue(se_ro):
                se_ro = []
            else:
                cnt += 1
                se_ro = []

    sa_gak_cnt = sa_gak_true(arr, 0, 0) + sa_gak_true(arr, 0, 3) + sa_gak_true(arr, 0, 6)
    + sa_gak_true(arr, 3, 0) + sa_gak_true(arr, 3, 3) + sa_gak_true(arr, 3, 6)
    + sa_gak_true(arr, 6, 0) + sa_gak_true(arr, 6, 3) + sa_gak_true(arr, 6, 6)

    if cnt + sa_gak_cnt == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')