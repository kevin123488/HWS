import sys
sys.stdin = open('1225_input.txt')

# arr를 조건에 맞춰 1사이클 돌려주는 함수
def cycle(arr):
    i = 1
    while i < 6:
        a = arr.pop(0)
        if a-i < 0:
            arr.append(a-i)
            break
        else:
            arr.append(a-i)
        i += 1
    return arr

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 받은 배열을 cycle 함수에 넣어 계속 돌리다가
    while True:
        cycle(arr)
        if 0 in arr: # 배열에 0이 나오면(cycle 돌다가 0보다 작은 값이 나와서 break된 상황)
            break    # 배열에 cycle함수 적용시켜주는거 그만

    for z in range(len(arr)):
        if arr[z] < 0:
            arr[z] = 0

    # 출력하자
    print(f'#{tc}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()