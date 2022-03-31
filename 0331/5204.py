import sys
sys.stdin = open('5204_input.txt')

# 병합정렬
# N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할
# 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다

def b_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    L_arr = arr[:middle]
    R_arr = arr[middle:]

    L_arr = b_sort(L_arr)
    R_arr = b_sort(R_arr)

    return merge(L_arr, R_arr)

def merge(Left, Right):
    global cnt
    result_list = []
    if Left[-1] > Right[-1]:
        cnt += 1
    lenleft = len(Left)
    lenright = len(Right)

    while lenleft > 0 or lenright > 0:
        if lenleft > 0 and lenright > 0:
            if Left[0] <= Right[0]:
                result_list += [Left[0]]
                Left = Left[1:]
                lenleft -= 1
            else:
                result_list += [Right[0]]
                Right = Right[1:]
                lenright -= 1
        elif lenleft > 0:
            result_list += [Left[0]]
            Left = Left[1:]
            lenleft -= 1
        elif lenright > 0:
            result_list += [Right[0]]
            Right = Right[1:]
            lenright -= 1

    return result_list

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 정수의 개수
    arr = list(map(int, input().split())) # 정렬해야 하는 요소들의 리스트

    cnt = 0
    ans = b_sort(arr)[N//2]

    print(f'#{tc} {ans} {cnt}')