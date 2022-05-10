# 주어진 N길이의 숫자열을 오름차순으로 정렬하라
# max 함수 만들기
import sys
sys.stdin = open('1966_input.txt')

def my_min(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr[-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 받은 arr을 오름차순으로 정렬하자
    sorted_arr = []
    while len(arr) > 0:
        sorted_arr += [my_min(arr)]
        arr.remove(my_min(arr))

    print(f'#{tc}', *sorted_arr)