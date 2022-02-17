import sys
sys.stdin = open('4865_글자수_input.txt')

# 테스트 케이스의 개수
T = int(input())

# count 함수 만들기
def count(args, find):
    count_1 = 0
    for arg in args:
        if arg == find:
            count_1 += 1
    return count_1

for tc in range(1, T+1):
    # 두개의 문자열이 주어짐
    str1 = input()
    str2 = input()
    # 문자열 str1에 들어있는 요소들이 str2에 몇개씩 들어있는지 확인, 가장 많은 글자의 개수를 출력하라

    set_str1 = []
    for i in str1:
        if i not in set_str1:
            set_str1 += [i]

    count_list = [0]
    for j in set_str1:
        count_list += [count(str2, j)]

    for z in range(len(count_list)-1):
        if count_list[z] > count_list[z+1]:
            count_list[z], count_list[z+1] = count_list[z+1], count_list[z]
    ans = count_list[-1]

    print(f'#{tc} {ans}')