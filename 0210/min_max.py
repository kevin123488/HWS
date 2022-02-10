import sys

sys.stdin = open('min_max_input.txt')

N = int(input()) # 테스트 케이스의 횟수를 받음

for tc in range(1, N+1): # 테스트 케이스의 수만큼 돌자
    num_num = int(input()) # 몇 개의 숫자를 받을지 확인
    num_list = list(map(int, input().split())) # 숫자 리스트를 받아옴
    num_list2 = num_list[:]

    for k in range(num_num-1): # 버블정렬로 최댓값 구할 생각임
        if num_list[k] >= num_list[k+1]:
            num_list[k+1], num_list[k] = num_list[k], num_list[k+1]

    for j in range(num_num-1): # 위와 같은 방법으로 최솟값 구함
        if num_list2[j] <= num_list2[j+1]:
            num_list2[j+1], num_list2[j] = num_list2[j], num_list2[j+1]

    print(f'#{tc} {num_list[-1] - num_list2[-1]}')