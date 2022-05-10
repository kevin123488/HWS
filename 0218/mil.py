# SWEA 1859번
# 최대한의 이득을 얻도록 ㄱ
# 연속한 N일 동안의 매매가를 알고 있다
# 하루에 최대 1만큼 구매 가능하다
# 판매는 얼마든지 할 수 있다
import sys
sys.stdin = open('mil_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    benefit = 0

    i = 0
    while i < N:
        if arr == []:
            break
        elif arr[i] == max(arr):
            benefit += i*max(arr)-sum(arr[:i])
            arr = arr[i+1:]
            i = 0
        else:
            i += 1

    print(f'#{tc} {benefit}')