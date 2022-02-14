import sys
sys.stdin = open('practice2_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 부분집합 만들기
    sub_set = [[]]

    for i in arr: # 받아온 리스트를 하나씩 순회
        len_subset = len(sub_set) # 부분집합의 길이를 변수에 담아준다
        for k in range(len_subset):
            sub_set.append(sub_set[k] + [i]) # 부분집합을 순회하며 arr의 값을 하나씩 넣어줌

    sub_set.pop(0) # 해당 문제를 풀기 위해 부분집합의 0번 인덱스(공집합)를 빼줌

    ans_sum_list = []
    for j in sub_set: # 부분집합 모둠 순회
        ans_sum = 0 # 부분집합 하나 돌때마다 부분집합의 합은 0으로 초기화
        for x in j: # 부분집합 개별적으로 순회
            ans_sum += x # 부분집합의 원소들을 더하는 과정
        ans_sum_list += [ans_sum] # 부분집합 합을 리스트에 담는 과정

    if 0 in ans_sum_list: # 만약 부분집합의 합이 모여있는 리스트 안에 0이 있다면
        print(f'#{tc} 1') # 1 출력
    else: # 없으면 0 출력
        print(f'#{tc} 0')