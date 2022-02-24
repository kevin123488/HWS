import sys
sys.stdin = open('4881_input.txt')

# N*N 배열을 받는다. 해당 배열에서 각 행당 1개, 열당 1개씩의 원소만 체크가 되도록 한 후 그 체크한 값들의 합이 가장 작은 경우를 구하여라.
# 함수
def only_one(arr, x, y):
    # 배열, 행, 열의 인덱스를 입력받아 해당 인덱스의 가로축 및 세로축의 요소들은 모두 0로 돌리는 함수
    for i in range(len(arr)):
        arr[x][i] = 0
    for j in range(len(arr)):
        arr[j][y] = 0
    return arr

def case_test(arr):
    global sum_thing
    index_to_find = [[1]*N for __ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if index_to_find[i][j] != 0:
                sum_thing += arr[i][j]
                only_one(index_to_find, i, j)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    index_to_find = [[1]*N for __ in range(N)]
    sum_thing = 0
    case_test(arr)

    print(f'#{tc} {sum_thing}')