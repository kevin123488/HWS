import sys
sys.stdin = open('5248.txt')

# 효율적인 방법을 생각해보자
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # arr를 2개씩 끊어 저장해보자
    wholikewho = []
    temp = []
    for i in arr:
        temp.append(i)
        if len(temp) == 2:
            wholikewho.append(temp)
            temp = []

    # wholikewho를 순회하며 하나의 리스트를 만들어보자
    ans_list = []
    temp2 = []
    for i in wholikewho:
