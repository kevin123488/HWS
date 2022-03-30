# 퀵 정렬
# 임의의 요소(피봇)을 정한다
# 피봇을 기점으로 작은 값은 왼쪽, 큰 값은 오른쪽에 위치시킨다
# -----, 피봇, ----- 와 같은 형태로 정렬이 되면
# -----와 -----를 다시 위의 방법으로 정렬한다
# 충분히 작은 배열이 되었을 때, 그 배열들을 병합하여 퀵정렬을 끝낸다

import sys
sys.stdin = open('input.txt')

def q_sort(arr):
    pivot = arr[0] # 정렬해야 하는 배열의 첫번째 값을 pivot이라고 설정
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            arr[i], arr[arr.index(pivot)] = arr[arr.index(pivot)], arr[i]
    # 위의 과정 끝났으면? pivot 전후의 arr부분에 대해서도 같은 과정을 반복해주자
    pivot_idx = arr.index(pivot)
    if pivot_idx == 0:
        q_sort(arr[1:])
    else:
        q_sort(arr[:pivot_idx])
        q_sort(arr[pivot_idx:])
    return arr

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    q_sort(arr)
    print(arr)