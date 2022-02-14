import sys
sys.stdin = open('snail_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # N값을 받았으니, N * N 행렬을 만들어보자
    arr = [[0]*N for _ in range(N)]
    count = 1
    for i in range(N):
        for j in range(N):
            arr[i][j] += count
            count += 1
    # arr 받아오기 성공
    # 받아온 arr을 달팽이 순서대로 재배열

    di = [0, 1, 0, -1] # 우, 하, 좌, 상
    dj = [1, 0, -1, 0] # 우, 하, 좌, 상
