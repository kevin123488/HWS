arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sub_set = [[]]

for i in arr:
    for k in range(len(sub_set)):
        sub_set.append(sub_set[k] + [i])

# print(sub_set)
print(len(sub_set))
a = 2**12
print(a)