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

def make_num2(a, b): # 숫자 a를 b진수로 표현
    if a >= b:
        s = a%b
        k = a//b
        make2_list.append(s)
        make_num(k, b)
    else:
        make2_list.append(a)
        # make2_list.reverse()
        return

make2_list = []

make_num2(4, 2)
# print(make2_list)
make2_list.reverse()
print(make2_list)