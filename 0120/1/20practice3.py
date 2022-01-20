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

def get_strong_word(str1, str2):
    sum_str1 = 0
    sum_str2 = 0
    for i in str1:
        a = ord(i)
        sum_str1 += a
    for k in str2:
        b = ord(k)
        sum_str2 += b
    if sum_str1 > sum_str2:
        return str1
    else:
        return str2

result = get_strong_word('z', 'a')
print(result)