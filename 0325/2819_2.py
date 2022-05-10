import sys
sys.stdin = open('2819.txt')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(num, y, x):
    global seven_dic
    if len(num) == 7:
        seven_dic[num] = 'Cindy'
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            num += arr[ny][nx]
            dfs(num, ny, nx)
            num = num[:-1]


T = int(input())
for tc in range(1, T + 1):
    seven_dic = {}
    arr = [list(input().split()) for _ in range(4)]

    for y in range(4):
        for x in range(4):
            num = arr[y][x]
            dfs(num, y, x)

    print(f'#{tc} {len(seven_dic)}')
    print(seven_dic)