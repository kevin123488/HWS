import sys
sys.stdin = open('1210_input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    start = arr[0][0]

    for i in range(100): # arr를 인덱스로 쭉 순회해주기
        for j in range(100): # (i, j)가 (0, 0)부터 (99, 99)까지
            if start == 1:
                if