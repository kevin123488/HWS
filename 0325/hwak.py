import sys
sys.stdin = open('2819.txt')
di = [0, 1, 0, -1] # 우하좌상
dj = [1, 0, -1, 0] # 우하좌상
def word_seven(a, b, seven_num):
    if len(seven_num) == 7:
        if seven_num not in ans_list:
            ans_list.append(seven_num)
            return
        else:
            return
    for i in range(4):
        ni = a + di[i]
        nj = b + dj[i]
        if 0 <= ni < 4 and 0 <= nj < 4: # 이동할 수 있는 곳이면
            seven_num += arr[ni][nj]
            word_seven(ni, nj, seven_num) # 이동하고 그 값 넣어줘라
            seven_num = seven_num[:-1]
T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    ans_list = []
    # 모든 위치에서 시작
    for i in range(4):
        for j in range(4):
            word_seven(i, j, arr[i][j]) # 모든 좌표에 대해 word_seven 함수를 실행해줌
            # word_seven 함수는 받은 좌표에서 시작해 총 6번 이동하고, 시작점을 포함하여 이동할때마다 seven_num에 해당 값을 넣어준다
    ans = len(ans_list)
    print(f'#{tc} {ans}')