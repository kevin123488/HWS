# def palindrome(args):
#     if args == args[-1::-1]:
#         return True
#     else:
#         return False
#
# arr = [1, 2, 3, 4, 5, 4, 3, 2, 5]
# ans = palindrome(arr)
# print(arr[-1::-1])
# print(ans)
# def my_max(ar):
#     for i in range(len(ar)-1):
#         if ar[i] > ar[i+1]:
#             ar[i], ar[i+1] = ar[i+1], ar[i]
#     return ar[-1]
#
# lis_t = []
# # lis_t += [1]
# # lis_t += [2]
# print(lis_t)
# ans = my_max(lis_t)
# print(ans)

# def sub_set(argss):
#     sub_set = [[]]
#     for z in argss:
#         for k in range(len(sub_set)):
#             sub_set.append(sub_set[k]+[z])
#     return sub_set
#
# print(sub_set([1, 2, 3, 4, 5, 6, 7]))

def palindrome(args):
    if args == args[-1::-1]:
        return True
    else:
        return False
print(palindrome([1, 2, 3, 5, 5, 4, 3, 2, 1]))