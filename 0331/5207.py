# 이진 탐색
# 서로다른 정수 N개를 정렬한 상태로 리스트A에 저장
# 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수 인지 이진 탐색을 통해 확인
# middle = (l+r)//2 (l은 탐색구간의 시작점, r은 탐색구간의 끝점)
# 이진탐색의 구간-> 왼쪽: arr[l:m], 오른쪽: arr[m:r+1]

import sys
sys.stdin = open('5207.txt')

def bi(a, arr): # 이진탐색 해주는 함수
    global ans
    s = 0 # 시작점의 인덱스
    f = len(arr)-1 # 끝점의 인덱스
    middle = (s+f)//2 # 이진탐색의 기준이 될 인덱스
    
    if f == -1: # 만약 조회하고자 하는 arr가 비어있다면?
        return None # None을 반환하자
    if arr[middle] > a: # 찾고자 하는 요소가 탐색중인 리스트의 middle 값보다 작다면
        bi(a, arr[:middle])
    elif arr[middle] < a: # 찾고자 하는 요소가 탐색중인 리스트의 middle 값보다 크다면
        bi(a, arr[middle+1:])
    else:
        ans += 1
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split())) # 리스트 a
    b_list = list(map(int, input().split())) # 리스트 b

    a_list.sort()
    # 이진 탐색으로 b_list의 요소들을 찾아보자

    ans = 0
    for i in b_list:
        bi(i, a_list)

    print(f'#{tc} {ans}')