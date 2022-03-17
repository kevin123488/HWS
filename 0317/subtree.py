# swea 5174

import sys
sys.stdin = open('subtree.txt')

def find(arr, v):
    global cnt
    for i in arr:
        if i[0] == v:
            cnt += 1
            find(arr, i[1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E는 간선의 개수, N은 시작 노드
    arr = list(map(int, input().split()))
    sub = []
    arr2 = []
    # arr를 2개씩 끊어서 2차원 리스트 안에 넣어주자
    for i in range(len(arr)):
        sub.append(arr[i])
        if len(sub) == 2:
            arr2.append(sub)
            sub = []

    cnt = 1
    find(arr2, N)
    print(f'#{tc} {cnt}')