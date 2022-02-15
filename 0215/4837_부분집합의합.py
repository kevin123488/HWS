import sys
sys.stdin = open('4837_부분집합의합_input.txt')

def my_sum(args):
    su_m = 0
    for num in args:
        su_m += num
    return su_m

# 먼저 부분집합을 구해보자
# 문제에서의 집합은 1~12까지의 숫자를 원소로 가진다. 그 집합의 부분집합은?
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sub_set = [[]]

for i in arr:
    for k in range(len(sub_set)):
        sub_set.append(sub_set[k] + [i]) # 부분집합을 구함

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    # n은 부분집합 원소의 수, k는 부분집합 원소의 합

    # 원소의 수가 n과 일치하는 부분집합을 따로 떼서 보자
    num_same_list =[]
    for j in sub_set:
        if len(j) == n:
            num_same_list += [j]

    count = 0
    for z in num_same_list:
        if my_sum(z) == k:
            count += 1

    print(f'#{tc} {count}')