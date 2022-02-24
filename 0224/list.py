arr = [1, 2, 3]
arr2 = [1] + arr

arr3 = [[0]+list(arr)+[0] for _ in range(3)]
arr3 = [[0]*5] + arr3 + [[0]*5]
print(arr3)