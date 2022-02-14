import sys
sys.stdin = open('practice1_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_ans = 0
    for i in range(N):
        for j in range(N):
            if 0 < i < N-1 and 0 < j < N-1:
                sum_ans += (abs(arr[i][j] - arr[i-1][j]) + abs(arr[i][j] - arr[i+1][j]) + abs(arr[i][j] - arr[i][j+1]) + abs(arr[i][j] - arr[i][j-1]))
            elif i == 0 and j == 0:
                sum_ans += (abs(arr[i][j] - arr[i][j+1]) + abs(arr[i][j] - arr[i+1][j]))
            elif i == 0 and j == N-1:
                sum_ans += (abs(arr[i][j] - arr[i][j - 1]) + abs(arr[i][j] - arr[i + 1][j]))
            elif i == N-1 and j == 0:
                sum_ans += (abs(arr[i][j] - arr[i-1][j]) + abs(arr[i][j] - arr[i][j+1]))
            elif i == N-1 and j == N-1:
                sum_ans += (abs(arr[i][j] - arr[i][j-1]) + abs(arr[i][j] - arr[i-1][j]))
            elif i == 0:
                sum_ans += (abs(arr[i][j] - arr[i][j-1]) + abs(arr[i][j] - arr[i][j+1]) + abs(arr[i][j] - arr[i+1][j]))
            elif j == 0:
                sum_ans += (abs(arr[i][j] - arr[i][j + 1]) + abs(arr[i][j] - arr[i+1][j]) + abs(
                    arr[i][j] - arr[i-1][j]))
            elif i == N-1:
                sum_ans += (abs(arr[i][j] - arr[i][j-1]) + abs(arr[i][j] - arr[i][j+1]) + abs(arr[i][j] - arr[i-1][j]))
            elif j == N-1:
                sum_ans += (abs(arr[i][j] - arr[i][j - 1]) + abs(arr[i][j] - arr[i+1][j]) + abs(arr[i][j] - arr[i-1][j]))
    print(sum_ans)