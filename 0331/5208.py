# 전기버스
# 정류장에는 교체용 충전지가 있는 교환기가 있음
# 충전지마다 최대로 운행 가능한 정류장 수가 정해져있음
# 충전기 방전 전에 교체하며 운행해야 함
# 교체 시간을 줄이려면 최소한의 교체 횟수로 이하생략
# 목적지에 도달하는데 필요한 최소한의 교환횟수 출력
# 출발지 배터리 장착은 교환에 포함되지 않음

# arr[0]-> 정류장 수
# arr[1:]-> 정류장 별 배터리 용량(도착 정류장 제외)
# 0번부터 N-2번까지(도착 정류장 제외) 충전지 정보

import sys
sys.stdin = open('5208.txt')

def find_ch(a, cnt): # 시작 정류장 a
    global ans
    if cnt > ans: # 가지치기 조건
        return
    for i in range(1, choong[a]+1): # 충전량만큼 이동 가능하므로, 1부터 충전량까지 대입
        if a+i == arr[0]: # 도착했을 때
            if ans > cnt: # ans(기존에 구해둔 값)와 cnt(연산중인 값)를 비교하여
                ans = cnt # ans값 갱신
            return
        else: # 도착 안했으면
            find_ch(a+i, cnt+1) # 다시 돌자

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    choong = [0] + arr[1:] # 함수에서 사용할 정류장의 충전지 정보, 인덱스의 번호와 정류장의 번호가 일치

    ans = 1000000
    find_ch(1, 0) # 1번 정류장(시작 정류장)에서 시작하여 찾아보자
    print(f'#{tc} {ans}')