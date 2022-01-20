# def get_secret_word(args):
#     l_ist = []
#     for i in args:
#         a = chr(i)
#         # print(type(a))

#         l_ist += a
#     sum_of_str = ''
#     for k in l_ist:
#         sum_of_str += k
#     return sum_of_str

# result = get_secret_word([83, 115, 65, 102, 89])
# print(result)

# def get_secret_word(args):
#     sum_of_str = ''
#     for i in args:
#         a = chr(i)
#         sum_of_str += a
#     return sum_of_str

# result = get_secret_word([83, 115, 65, 102, 89])
# print(result)

# def get_secret_number(args):
#     sum_of_num = 0
#     for i in args:
#         a = ord(i)
#         sum_of_num += a
#     return sum_of_num

# print(get_secret_number('tom'))

# def get_strong_word(str1, str2):
#     sum_str1 = 0
#     sum_str2 = 0
#     for i in str1:
#         a = ord(i)
#         sum_str1 += a
#     for k in str2:
#         b = ord(k)
#         sum_str2 += b
#     if sum_str1 > sum_str2:
#         return str1
#     else:
#         return str2

# result = get_strong_word('z', 'a')
# print(result)

# 회문 판별
# 1. while 사용
# def is_pal_while(word):
#     length = 0
#     for i in word:
#         length += 1
#     k = 0
#     wor_d = ''
#     while k < length:
#         wor_d += word[-k-1]
#         k += 1
#     if wor_d == word:
#         return True
#     else:
#         return False

# print(is_pal_while('tomato'))
# print(is_pal_while('racecar'))
# print(is_pal_while('azza'))

# 2. 재귀함수 이용
# def is_pal_recursive(word):

# 교수님 답변(회문판별)
# def is_pal_while(word):
#     while len(word) > 1:
#         # 첫 글자와 마지막 글자를 비교
#         if word[0] == word[-1]:
#             # 같다면? 다음단계 ㄱ
#             # 조사할 word 바꿔치기
#             word = word[1: -1]
#             pass
#         else:
#             return False
#     return True

# 교수님 답변(회문-재귀함수)

# def is_pal_recursive(word):
#     # 1. 종료 조건
#     # 단어 길이가 1보다 작아졌다면 회문, True 반환
#     if len(word) <= 1:
#         return True

#     # word 조사 시작
#     if word[0] == word[-1]:
#         return is_pal_recursive(word[1:-1])
#     # 한번이라도 다르면
#     else:
#         return False

# 재귀함수 다시 보기!!