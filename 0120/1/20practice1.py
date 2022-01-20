# my_abs() 작성하기

# def my_abs(x):
#     if type(x) == complex:
#         return ('복소순데')
#     elif x > 0:
#         return x
#     elif x == 0:
#         return x+1-1
#     else:
#         return -x

# ans = my_abs(-5)
# print(ans)
# print(my_abs(-0.0))
# print(my_abs(3+4j))
# print(abs(3+4j), abs(-0.0), abs(-5))

# def my_all(args):
#     if args == []:
#         return True
#     else:
#         for i in args:
#             if i == []:
#                 return True
#             else:
#                 return False

# print(my_all([]))
# print(my_all([1, 2, 5, '6']))
# print(my_all([[], 2, 5, '6']))

# def my_any(args):
#     if args == [0]:
#         return False
#     else:
#         return True

# print(my_any([1, 2, 5, '6']))
# print(my_any([[], 2, 5, '6']))
# print(my_any([0]))

# 1번 교수님 답안
# def my_abs(x):
#     # 복소수라면
#     if type(x) == complex:
#         (x.imag ** 2 + x.real ** 2) ** (1/2)
#     else:
#         if x < 0:
#             return -x
#         elif x == 0:
#             return x ** 2
#         else:
#             return x

# 2번 교수님 답안
# 하나씩 비교하며 참인지 아닌지 판별
# def my_all(elements):
#     for el in elements:
#         if el == True:
#             pass
#         else:
#             return False
# def my_all(elements):
#     for el in elements:
#         if not el:
#             return False
#     return True

# 3번 교수님 답안
# def my_any(elements):
#     for el in elements:
#         if el:
#             return True
#     return False

# all([]) -> true
# any([]) -> False