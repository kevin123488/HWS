import sys
sys.stdin = open('4880.txt')

def boonhal(arr):
    start = 0 # 시작점 인덱스
    end = len(arr)-1 # 끝점 인덱스
    # 분할지점을 잠아야 함. 슬라이싱을 이용
    middle = (start + end)//2
    if start == end:
        return 1
    else:
        arr1 = arr[start:middle+1]
        arr2 = arr[middle+1:]
        boonhal(arr1)
        boonhal(arr2)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(boonhal(arr))