import sys
sys.stdin = open('2819.txt')

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b, num):
    global ans_list
    if len(num) == 7:
        if num in ans_list: # 겹치는 친구들은 추가 안함
            return
        else:
            ans_list.append(num) # ans_list에 안들어있는 애들은 추가해줌
            return

    for i in range(4): # 델타탐색 시작
        ni = a + di[i]
        nj = b + dj[i]
        if 0 <= ni < 4 and 0 <= nj < 4:
            num += arr[ni][nj]
            dfs(ni, nj, num)
            num = num[:-1]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans_list = [] # 정답을 담을 리스트

    for i in range(4):
        for j in range(4): # 4*4 배열을 전부 순회하며 시작점 바꿔가자
            num = arr[i][j] # 7자리를 담기 위한 리스트. 시작점을 담아주고 시작하자
            dfs(i, j, num) # dfs 돌자

    print(f'#{tc} {len(ans_list)}')
    print(ans_list)