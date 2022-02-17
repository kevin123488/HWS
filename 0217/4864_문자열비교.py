import sys
sys.stdin = open('4864_문자열비교_input.txt')

# 테스트 케이스의 개수 T가 주어짐
T = int(input())
for tc in range(1, T+1):
    str1 = input() # 짧은 문자열
    str2 = input() # 긴 문자열

    count_1 = [0]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if j+len(str1) <= len(str2): # <=인 이유는 len(str2)와 같은 값일때 str2의 마지막 부분에 걸치기 때문
                    if str1 == str2[j:j+len(str1)]: # 이렇게 조회하면 j번째 인덱싱부터 len(str1)만큼의 길이의 문자열을 조회 가능함
                        count_1 += [1]

    if count_1 == [0]:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')