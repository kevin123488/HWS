import sys
sys.stdin = open('특별한정렬_input.txt')
# N개의 정수가 주어졌을 때 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬
# 그 결과를 10개까지 출력
# 버블정렬 후 -1, 0, -2, 2, -3, 3, -4, 4, -5, 5 출력하면?

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 이 수만큼의 배열을 받음
    arr = list(map(int, input().split())) # N 다음에 오는 수 나열 받음

    # 버블정렬로 arr 오름차순 배열
    for i in range(N):
        for z in range(N-i-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]

    # arr의 [-1], [1], [-2], [2], ..... 를 빈 리스트에 추가해준 후 * 하면?
    ans_list = []
    for k in range(1, 6):
        ans_list.append(arr[-k])
        ans_list.append(arr[k-1])

    ans = ' '.join(map(str, ans_list))
    print(f'#{tc} {ans}')