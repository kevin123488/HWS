import sys
sys.stdin = open('색칠하기_input.txt')

# 10*10 격자에 빨간색과 파란색을 칠한다
T = int(input())
# arr = [[0]*10 for _ in range(10)] # 10*10 격자 만듬

for tc in range(1, T+1): # 테스트케이스만큼 순회
    N = int(input()) # 네모 몇개 받을지 확인하기
    arr = [[0] * 10 for _ in range(10)]  # 10*10 격자 만듬 # 얘 위치 주의하자
    for i in range(N): # 네모 개수만큼 색칠해주기
        i1, j1, i2, j2, color = map(int, input().split()) # 네모의 좌표값 받아오기
        for j in range(10): # 인덱싱
            for k in range(10): # 인덱싱
                if i1 <= j <= i2 and j1 <= k <= j2: # 상자의 범위
                    if arr[j][k] == 0: # 색칠 안돼있으면
                        arr[j][k] += color # 색칠해
                    elif arr[j][k] == 1: # 빨간색이면
                        if color == 2: # 파란색일때만
                            arr[j][k] += color # 색칠해
                    elif arr[j][k] == 2: # 파란색이면
                        if color == 1: # 빨간색일때만
                            arr[j][k] += color # 색칠해

    count = 0
    for z in arr:
        for s in z:
            if s == 3:
                count += 1

    print(f'#{tc} {count}')