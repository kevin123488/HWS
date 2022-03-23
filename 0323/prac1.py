import sys
sys.stdin = open('prac1.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()

    # 7개씩 끊어서 계산
    length = len(arr) // 7
    for i in range(length):
        n = 0
        for j in range(i*7, i*7+7):
            n = n*2 + int(arr[j])
        print(n, end=' ')
    print()