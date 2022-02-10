import sys

sys.stdin = open('num_card_input.txt')

N = int(input()) # 테스트 케이스 개수
for tc in range(1, N+1): # 테스트 케이스 개수만큼 순회
    num_card = int(input()) # 카드 장 수 입력받음
    num_card_list = list(map(int, input()))
    num_card_list2 = num_card_list[:]
    # 입력받는 수들을 카운트하는 리스트가 필요
    # 입력받는 값들 중 가장 큰 값을 기준으로 + 1 한 수만큼 [0]을 만들어주면 될 듯
    for i in range(len(num_card_list2) - 1):
        if num_card_list2[i] > num_card_list2[i+1]:
            num_card_list2[i], num_card_list2[i+1] = num_card_list2[i+1], num_card_list2[i]

    num_max = num_card_list2[-1]
    count_list = [0] * (num_max + 1)

    for j in num_card_list:
        count_list[j] += 1

    max_count = 0 # 최빈값의 빈도를 찾아냄
    max_num_list = [] # 범위가 양의 정수이므로
    for k in range(len(count_list)):
        if max_count <= count_list[k]:
            max_count = count_list[k]
            max_num_list += [k]
    max_num = -1
    for h in max_num_list:
        if max_num < h:
            max_num = h
    print(f'#{tc} {max_num} {max_count}')