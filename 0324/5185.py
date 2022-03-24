# swea 5185
# 이진수
import sys
sys.stdin = open('5185.txt')

def make_num(a, b): # 숫자 a를 b진수로 표현
    if a >= b:
        s = a%b
        k = a//b
        make2_list.append(s)
        make_num(k, b)
    else:
        make2_list.append(a)
        # make2_list.reverse()
        return

T = int(input())
for tc in range(1, T+1):
    N, num = input().split() # N: 16진수의 자릿수, num: 16진수로 표현된 입력값

    ans_list = []

    make2_list = []
    for i in num:
        if i == 'A':
            make_num(10, 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []
        elif i == 'B':
            make_num(11, 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []
        elif i == 'C':
            make_num(12, 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []
        elif i == 'D':
            make_num(13, 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []
        elif i == 'E':
            make_num(14, 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []
        elif i == 'F':
            make_num(15, 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []
        else:
            make_num(int(i), 2)
            make2_list.reverse()
            ans_list.append(make2_list)
            make2_list = []

    for j in ans_list:
        if len(j) < 4:
            while len(j) != 4:
                j = [0] + j

    print(f'#{tc} ', end='')
    for k in ans_list:
        for z in k:
            print(z, end='')

    print()