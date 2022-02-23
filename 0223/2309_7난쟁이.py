import sys
sys.stdin = open('2309_input.txt')

height_list = []
for i in range(1, 10):
    i = int(input())
    height_list += [i]

# 해당 키 리스트중 7개를 뽑아 합이 100이 나오는 경우의 리스트를 골라야 한다.
# 부분집합을 구한 후, 그 중 길이가 7인 집합을 모아보자

sub_set = [[]]
for i in height_list:
    leng_th = len(sub_set)
    for k in range(leng_th):
        sub_set.append(sub_set[k] + [i])

the_real_ans_list = []
for j in sub_set:
    if len(j) == 7:
        the_real_ans_list += [j]

the_the_real_ans_list = []
for l in the_real_ans_list:
    if sum(l) == 100:
        the_the_real_ans_list += [l]

the_the_real_ans_list[0].sort()
for a in the_the_real_ans_list[0]:
    print(a)