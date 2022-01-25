# 정중앙 문자를 반환하는 함수
# 만약 문자열의 길이가 짝수라면, 중앙의 2개를 반환
# 함수를 정의
# 전달인자를 받을 매개변수
# def get_middle_char(word):
#     length = 0
#     # 단어 전부 순회하며 갯수 세기
#     for i in word:
#         length += 1
#     # 정 중앙값
#     center = length // 2

#     # 만약 홀수라면
#     if length % 2:
#         result = word[center]
#     # 짝수라면
#     else:
#         result = word[center-1:center+1]
#     return result

# answer = get_middle_char('ssafy')
# print(answer)

# 함수 정의
# 가변 인자 리스트 -> 다수의 인자들을 한번에 받아보자

def my_avg(*numbers):
    length = 0
    count = 0
    for i in numbers:
        length += 1
        count += i
    return count // length
result = my_avg(77, 83, 95, 80, 70)
print(result)