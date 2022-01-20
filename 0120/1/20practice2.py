# 기둥의 높이, 올라가는 거리, 미끄러지는 거리
# snail(높이, 올거리, 미거리)

# def snail(height, day, night):
#     return round(height/(day - night))

# print(snail(100, 5, 2))

# def sum_of_digit(args):
#     length = len(str(args))
#     sum = 0
#     for i in range(length):
#         plus = args % 10^(i+1)
#         sum += plus
#     return sum

# print(sum_of_digit(1234))
# print(sum_of_digit(4321))

# a = 1234
# print(str(a)[1])

# def sum_of_digit(args):
#     length = len(str(args))
#     sum = 0
#     for i in range(length):
#         plus = (args//10**i)%10
#         sum += plus
#     return sum
# print(sum_of_digit(1234))
# print(sum_of_digit(4321))

# 교수님 답변 (달팽이 문제)
# def snail(height, day, night):
#     #달팽이가 꼭대기에 도달하는 날을 찾기
#     #꼭대기에 도달한 그 날을 출력
#     #낮동안 올라감, 밤동안 미끄러짐
#     count = 0
#     #하룻동안 올라간 거리
#     dis = 0
#     while dis <= height: # while True 해도 ㄱㅊ. 밑에 종료조건 있으니까
#         # 첫날 + 매일 하루씩 지나감
#         count += 1
#         dis += day
#         #낮동안 올라가고 난 다음 위치 조사
#         if dis >= height: #종료조건
#             return count
#         dis -= night

# 교수님 답변 (자릿수 더하기)

# 각 자릿수를 알아내야 한다
# 어떻게?
# 1234가 왔을 때, 1, 10, 100, 1000의 자리의 값을 받아야 한다.

# def sum_of_digit(number):
#     result = 0
#     while number / 10:
#         remainder = number % 10
#         result += remainder
#         # 원본 값을 10으로 나눈 몫ㅇ로 바꿔치기
#         number = number // 10
#     return result

# 재귀함수 버전
# def sum_of_recursive(number):
#     # 종료조건
#     if number < 10:
#         return number
#     else:
#         # 나머지 구하기
#         remainder = number % 10
#         # 원본 숫자는 10으로 나눈 몫만 남기기
#         number = number // 10
#         return sum_of_recursive(number) + remainder

# print(sum_of_recursive())