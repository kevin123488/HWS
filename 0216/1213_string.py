import sys
sys.stdin = open('1213_string_input.txt', encoding='UTF-8')

# 전체 테스트케이스 수 10개
for tc in range(1, 11):
    T = int(input())
    find = input()
    string = input()

    # string을 조회하며 find와 일치하는 부분이 얼마나 있는지 확인해야 함
    # 이중포문으로 조회하자.
    count = 0
    for i in range(len(find)):
        for j in range(len(string)): # find의 첫 글자에 대해 j를 쭉 순회. 만약 같으면? find의 길이만큼 슬라이싱한 후 비교. 같으면? count += 1
            if find[i] == string[j]:
                if j+len(find) <= len(string): # 인덱싱 에러 방지, 범위 설정해줌
                    if find == string[j:j+len(find)]:
                        count += 1
    print(f'#{tc} {count}')