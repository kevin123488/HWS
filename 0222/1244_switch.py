import sys
sys.stdin = open('1244.txt')

switch_length = int(input())
switch_list = list(map(int, input().split()))
student_num = int(input())

for st in range(1, student_num+1):
    gender, switch_num = map(int, input().split())

    if switch_num - 1 == switch_length - switch_num:
        leeength = len(switch_list)//2
    elif switch_num - 1 > switch_length - switch_num:
        leeength = switch_length - switch_num
    else:
        leeength = switch_num-1

    if gender == 1: # 남자일 때
        # switch_num의 배수에 해당하는 위치의 스위치를 눌러준다
        for i in range(len(switch_list)):
            if (i+1)/switch_num == (i+1)//switch_num:
                if switch_list[i] == 0:
                    switch_list[i] = 1
                else:
                    switch_list[i] = 0

    else: # 여자일 때
        # switch_num에 해당하는 switch의 전후를 세트로 조회하며 회문 -> 눌러줌
        for k in range(leeength+1):
            if switch_list[switch_num-1-k] == switch_list[switch_num-1+k]:
                if switch_list[switch_num - 1 - k] == 0:
                    switch_list[switch_num - 1 - k] = 1
                    switch_list[switch_num - 1 + k] = 1
                else:
                    switch_list[switch_num - 1 - k] = 0
                    switch_list[switch_num - 1 + k] = 0
            else:
                break

# 출력 방식이 관건
# 20개씩 끊어서 출력해야 한다
# 20개 이하일 경우는? 그냥 출력
# 20개 초과일 경우는? 리스트에서 값을 20개 단위로 빼 또다른 리스트를 2차원으로 만들어보자

if len(switch_list) <= 20:
    print(*switch_list)
else:
    long = len(switch_list)//20
    for ii in range(long+1):
        print(*switch_list[20*ii:20*(ii+1)])