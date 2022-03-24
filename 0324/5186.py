import sys
sys.stdin = open('5186.txt')

def float_2(N):
    global float_2_list
    a = N*2
    float_2_list += [str(a)[0]]
    if len(float_2_list) == 13:
        return float_2_list
    if a > 1:
        a -= 1
        float_2(a)
    else:
        a = a
        float_2(a)

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    float_2_list = []

    float_2(num)
    ans_list = []
    for i in float_2_list:
        if int(i) == 2:
            pass
        else:
            ans_list += [int(i)]

    if len(ans_list) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} ', end='')
        for k in ans_list:
            print(k, end='')
        print()