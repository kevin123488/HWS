from re import I
import sys
sys.stdin = open('prac3.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()

    bit = ''
    
    for i in range(len(arr)):
        tmp = int(arr[i], 16)
        tmp = bin(tmp).replace('0b', '')
        
        while len(tmp) != 4:
            tmp = '0' + tmp
        bit += tmp
    
    for j in range(len(bit)-1, -1, -1):
        if bit[j] == 1:
            point = i
            break
    
    password = {
        '001101' : 0,
        '010011' : 1,
        '111011' : 2,
        '110001' : 3,
        '100011' : 4,
        '110111' : 5,
        '001011' : 6,
        '111101' : 7,
        '011001' : 8,
        '101111' : 9
}
    result = ''
    while point - 6 > 0:
        if bit[point-5:point+1] in password:
            # 뒷번호부터 더해 나가려면
            result = ' ' + str(password[bit[point-5:point+1]]) + result

            # 패턴 찾았으니 다음 패턴 조사
            point -= 6
        else:
            # 못 찾은 상황에 대해서 다른 조건들
            # 더 만들어서 처리하는것도 가능
            point -= 1

    print(result)