import sys
sys.stdin = open('2819.txt')

# 델타탐색
di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1] # 상하좌우

def dfs(a, b, num_list):
    global ans_list
    if len(num_list) == 7:
        ans_list.append(num_list)
        return
    for k in range(4):
        ni = a + di[k]
        nj = b + dj[k]
        if 0<=ni<4 and 0<=nj<4:
            num_list += [arr[a][b]]
            dfs(ni, nj, num_list)
            num_list = num_list[:-1]

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    ans_list = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, [arr[i][j]])

    ans = len(set(ans_list))
    print(f'${tc} {ans}')