# 부분집합 구하기
def setsetset(arr):
    sub_set = [[]]
    for i in arr:
        # len_ = len(sub_set)
        for j in range(len(sub_set)):
            sub_set.append(sub_set[j] + [i])
    return sub_set

arr = [1, 2, 3, 4]
a = setsetset(arr)
print(a)