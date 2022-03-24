import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # arr[i] -> i번째 행에 해당하는 '문자열'

    # 암호부분이 16진수로 적혀있다. 우선 이 16진수 부분을 2진수로 바꿔주어야 한다
    # 2진수로 바뀌면 역순으로 조회하며 1로 시작하는 부분을 찾자
    # 해당 암호코드의 길이는 (7+1), (14+1), (21+1) . . . 과 같은 느낌으로 이뤄질 것

    password = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    bin2 = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    find_list = []
    for i in range(N):
        for k in range(M-1, -1, -1):
            if arr[i][k] in 'A, B, C, D, E, F, 1, 2, 3, 4, 5, 6, 7, 8, 9' and arr[i-1][k] == '0':
                find_list.append(arr[i])
                break

    ans_list = []
    # find_list에 암호가 들어있는 줄을 넣어둠
    for i in range(len(find_list)):
        for k in range(len(find_list[i])):
            if find_list[i][k] == 'A':
                ans_list.append(bin2['A'])
            elif find_list[i][k] == 'B':
                ans_list.append(bin2['B'])
            elif find_list[i][k] == 'C':
                ans_list.append(bin2['C'])
            elif find_list[i][k] == 'D':
                ans_list.append(bin2['D'])
            elif find_list[i][k] == 'E':
                ans_list.append(bin2['E'])
            elif find_list[i][k] == 'F':
                ans_list.append(bin2['F'])
            else:
                ans_list.append(bin2[find_list[i][k]])

    # pprint(f'#{tc} {ans_list}')
    # 암호블럭의 가장 윗부분만 가져옴. 그 윗부분의 16진수를 2진수로 표현한 값을 문자열의 형태로 리스트에 넣어줬음
    # 예를들어 암호코드의 부분이 1234AA일 경우 ['0001', '0010', '0011', '0100', '1010', '1010']
    # 쟤를 역순으로 조회하면서 1이 조회될 경우 56n의 길이만큼 슬라이싱 해 해당 요소의 암호 적부를 판단하여야 한다(암호코드의 첫번째 줄에 해당하는 문자열보다 적은 범위 내에서)
    # (56개, 112개, ... 씩 끊어서 확인해보면 될듯)
    # 만약 적합하다면 break 한 후 해당 암호코드의 10진수 ver의 합을 출력하면 된다

    