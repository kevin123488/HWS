# 퀵정렬
# 퀵소트의 특징
# pivot의 설정
# pivot을 기준으로 그것보다 큰 그룹과 작은 그룹을 나눔
# 작은 그룹에 대해서 다시 pivot - 나누기
# 큰 그룹에 대해서 다시 pivot - 나누기
import sys
sys.stdin = open('5205.txt')

def q_sort(arr):
    if len(arr) <= 1: # 정렬대상의 요소가 1개이거나 없으면? 정렬해줄 필요 없다
        return arr
    middle = len(arr)//2
    pivot = arr[middle] # pivot 설정
    left_arr = []
    pivot_arr = []
    right_arr = []

    for i in arr: # arr를 순회하며
        if i < pivot: # pivot보다 적은 값이면
            left_arr.append(i) # 왼쪽 그룹에 넣어
        elif i > pivot: # pivot보다 큰 값이면
            right_arr.append(i) # 오른쪽 그룹에 넣어
        else:
            pivot_arr.append(i)

    # 위의 과정을 통해 왼쪽 그룹, 피봇, 오른쪽 그룹이 형성됨
    return q_sort(left_arr) + pivot_arr + q_sort(right_arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {q_sort(arr)[N//2]}')