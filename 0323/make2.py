# 진법계산 함수

def make_num(a, b): # 숫자 a를 b진수로 표현
    if a >= b:
        s = a%b
        k = a//b
        make2_list.append(s)
        make_num(k, b)
    else:
        make2_list.append(a)
        return make2_list

make2_list = []

make_num(64, 19)
# print(make2_list)
for i in range(len(make2_list)-1, -1, -1):
    print(make2_list[i], end='')