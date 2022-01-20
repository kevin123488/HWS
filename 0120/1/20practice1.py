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