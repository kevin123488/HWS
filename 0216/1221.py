import sys
sys.stdin = open('1221_input.txt')

# 테스트 케이스의 개수
T = int(input())
# 테스트 케이스의 개수만큼 돌림
for tc in range(1, T+1):
    # 테스트 케이스의 길이
    tc_num, N = input().split() # 테스트케이스의 번호와 길이를 받아오자 # 나중에 N에 int 씌워주는거 까먹지 말자
    arr = list(input().split()) # 문자열을 받아 리스트에 저장하자. 그 길이는 int(N)과 같을 것

    # ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN을 각각 0, 1, 2, 3, 4, 5, 6, 7, 8, 9에 대응시키자
    # 그 후 받은 리스트의 값들을 하나씩 숫자로 바꾸어주자
    ans_list = []
    for i in arr: # 이렇게 순회하면 문자열이 하나씩 조회됨. 우리가 원하는건 변수로서의 항목들임
        if i == 'ZRO':
            i = 0
        elif i == 'ONE':
            i = 1
        elif i == 'TWO':
            i = 2
        elif i == 'THR':
            i = 3
        elif i == 'FOR':
            i = 4
        elif i == 'FIV':
            i = 5
        elif i == 'SIX':
            i = 6
        elif i == 'SVN':
            i = 7
        elif i == 'EGT':
            i = 8
        elif i == 'NIN':
            i = 9
        ans_list += [i]

    ans_list.sort()

    the_real_ans_list = []
    for k in ans_list:
        if k == 0:
            k = 'ZRO'
        elif k == 1:
            k = 'ONE'
        elif k == 2:
            k = 'TWO'
        elif k == 3:
            k = 'THR'
        elif k == 4:
            k = 'FOR'
        elif k == 5:
            k = 'FIV'
        elif k == 6:
            k = 'SIX'
        elif k == 7:
            k = 'SVN'
        elif k == 8:
            k = 'EGT'
        elif k == 9:
            k = 'NIN'
        the_real_ans_list += [k]
        ans_ans = ' '.join(the_real_ans_list)

    print(f'{tc_num} {ans_ans}')