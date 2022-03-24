import sys
sys.stdin = open('5185.txt')

T = int(input())
for tc in range(1, T+1):
    N, num = input().split() # N: 자릿수, num: 16진수로 표현된 수

    ans_list = []
    for i in num:
        if i in 'ABCDEF':
            if i == 'A':
                ans_list += [bin(10)]
            elif i == 'B':
                ans_list += [bin(11)]
            elif i == 'C':
                ans_list += [bin(12)]
            elif i == 'D':
                ans_list += [bin(13)]
            elif i == 'E':
                ans_list += [bin(14)]
            elif i == 'F':
                ans_list += [bin(15)]
        else:
            ans_list += [bin(int(i))]

    # print(ans_list)
    print(f'#{tc} ', end='')

    # 문제가 요구하는 자리당 길이는 4
    for k in range(len(ans_list)):
        if len(ans_list[k]) == 6:
            print(ans_list[k][2:], end='')
        elif len(ans_list[k]) == 5:
            print('0', end='')
            print(ans_list[k][2:], end='')
        elif len(ans_list[k]) == 4:
            print('00', end='')
            print(ans_list[k][2:], end='')
        elif len(ans_list[k]) == 3:
            print('000', end='')
            print(ans_list[k][2], end='')

    print()