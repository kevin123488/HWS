import sys
sys.stdin = open('2116.txt')

def joosa_max(arr, idx):
    if idx == 0:
        return max(0, arr[1], arr[2], arr[3], arr[4], 0)
    elif idx == 1:
        return max(arr[0], 0, arr[2], 0, arr[4], arr[5])
    elif idx == 2:
        return max(arr[0], arr[1], 0, arr[3], 0, arr[5])
    elif idx == 3:
        return max(arr[0], 0, arr[2], 0, arr[4], arr[5])
    elif idx == 4:
        return max(arr[0], arr[1], 0, arr[3], 0, arr[5])
    elif idx == 5:
        return max(0, arr[1], arr[2], arr[3], arr[4], 0)

N = int(input()) # 주사위 갯수
joosa_list = [list(map(int, input().split())) for _ in range(N)] # 각 주사위들의 숫자 정보를 받음

max_answer_list = []
max_ans = 0
# 맞닿는 면의 수가 같도록 주사위를 쌓는다
# 1. 첫 주사위의 맞닿는 면이 joosa_list[0][0]일 경우의 최댓값을 max_answer_list에 넣어보자
# 2. 첫 주사위의 맞닿는 면이 joosa_list[0][1]일 경우의 최댓값을 max_answer_list에 넣어보자
# 3. 첫 주사위의 맞닿는 면이 joosa_list[0][2]일 경우의 최댓값을 max_answer_list에 넣어보자
# 4. 첫 주사위의 맞닿는 면이 joosa_list[0][3]일 경우의 최댓값을 max_answer_list에 넣어보자
# 5. 첫 주사위의 맞닿는 면이 joosa_list[0][4]일 경우의 최댓값을 max_answer_list에 넣어보자
# 6. 첫 주사위의 맞닿는 면이 joosa_list[0][5]일 경우의 최댓값을 max_answer_list에 넣어보자
# 모든 시작점에 따라 오직 한가지의 최댓값을 가진다.
# 첫 주사위의 윗면 인덱스가 3이다 -> 해당 값과 같은 값을 가지는 두번째 주사위의 면의 인덱스와, 그 맞은편의 인덱스를 찾고, 그 두개의 인덱스를
# 제외한 나머지중 최댓값을 max_ans에 더한 후 다음 단계(다음 주사위의 아랫면과 현재 주사위의 윗면이 같도록)

print(joosa_max(joosa_list[0], 1))
print(joosa_list[0].index(joosa_max(joosa_list[0], 1)))