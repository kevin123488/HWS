# 베이비진 게임
import sys
sys.stdin = open('input_5203.txt')

# run인지 triple인지 아무것도 아닌지 판별해주는 함수
def de_fine_tri(arr): # arr를 입력받아 해당 arr의 점수를 판단
    for i in range(len(arr)):
        if arr.count(arr[i]) >= 3:
            return 1
    return 0

def de_fine_run(arr):
    for i in range(len(arr)):
        if arr[i]-1 in arr and arr[i]+1 in arr:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 0부터 9까지의 숫자카드 4세트를 섞은 후 6장을 뽑자
    # 연속인 숫자가 3개 이상 -> run
    # 같은 숫자가 3개 이상 -> triple
    # 게임 시작하면 p1과 p2가 1장씩 카드를 가져감
    # 먼저 run이나 triple을 달성하는 사람이 이김

    p1 = [] # player 1이 가져가는 카드
    p2 = [] # player 2가 가져가는 카드
    for i in range(6):
        p1.append(arr[i*2])
        p2.append(arr[i*2+1])
        if len(p1) >= 3: # 3장 이상의 카드를 배부받았을 때
            if de_fine_run(p1) or de_fine_tri(p1): # p1이 걸렸다?
                print(f'#{tc} 1') # 바로 1번이 이기고 경기 종료(밸런스 패치 시급)
                break
            elif de_fine_run(p2) or de_fine_tri(p2): # 만약 p1이 안걸렸는데 p2가 걸렸다면?
                print(f'#{tc} 2') # p2가 이긴거니까 2 출력
                break
        if len(p1) == 6: # 다 뽑았을 때
            print(f'#{tc} 0')