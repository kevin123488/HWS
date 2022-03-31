# 이진 탐색
# 서로다른 정수 N개를 정렬한 상태로 리스트A에 저장
# 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수 인지 이진 탐색을 통해 확인
# middle = (l+r)//2 (l은 탐색구간의 시작점, r은 탐색구간의 끝점)
# 이진탐색의 구간-> 왼쪽: arr[l:m], 오른쪽: arr[m:r+1]

import sys
sys.stdin = open('5207.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # 처음 풀 땐 함수를 만들어 추가해줬다. 재귀의 형태로 들어가게 되었는데, 그 경우
    # cnt를 올려주는 조건을 넣기가 어려웠다. 그래서 반복문의 형태로 다시 풀어보려 한다

    ans = 0
    for i in b_list: # 리스트 b의 요소들을 대상으로 순회하자
        s = 0 # 시작지점
        f = len(a_list) # 끝지점
        flag = 0 # 비교해줄 때 쓸 것
        # while문 시작
        while s <= f: # 시작점과 끝점이 일치할 때 까지(원소가 1개 남을때까지) 돌자
            middle = (s+f)//2 # 중간지점을 설정해주자
            # b_list에서 조회중인 수와 middle 인덱스에 해당하는 값을 비교해야 한다
            if i > a_list[middle]: # 만약 찾고자 하는 수가 중간값보다 크다면?
                s = middle + 1 # 시작지점을 그 중간 인덱스보다 1 높인 곳으로 재설정
                if flag == 0:
                    flag = 1
                elif flag == 2: # 이전에 뒷 케이스를 적용했었다면 flag가 2가 되어있을 것
                    flag = 10
            elif i < a_list[middle]: # 만약 찾고자 하는 수가 중간값보다 작다면?
                f = middle - 1 # 끝지점을 그 중간 인덱스보다 1 낮춘 곳으로 재설정
                if flag == 0:
                    flag = 2
                elif flag == 1: # 이전에 앞 케이스를 적용했었다면 flag가 1이 되어있을 것
                    flag = 10

            else: # i값과 중간값이 같다면?
                if flag == 10: # 케이스별로 교차되면 flag 10으로 고정
                    ans += 1
                break

    print(f'#{tc} {ans}')