arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

real_list = []
lis_t = []
for j in range(3):
    for i in range(3):
        lis_t += [arr[i][j]]
        if len(lis_t) == 3:
            real_list += [lis_t]
            lis_t = []
print(real_list)