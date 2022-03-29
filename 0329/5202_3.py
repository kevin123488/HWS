# 화물 도크
import sys
sys.stdin = open('input_5202.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 화물의 이용 시간 정보를 담아둠
    # 빨리 끝나는 애들부터 넣어주자

    i = 1
    while len(arr) - i != 0:
        for k in range(len(arr) - i):
            if arr[k][1] > arr[k + 1][1]:  # 끝나는 시간이 늦는 애를 뒤로 보내주자
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
        i += 1
    # print(f'#{tc} {arr}')
    ans_list = [arr[0]] # 제일 먼저 끝나는 애를 넣어줌
    for i in range(1, N):
        if arr[i][0] < ans_list[-1][1]:  # 시간이 겹침
            continue
        else:  # 시간이 겹치지 않음
            ans_list.append(arr[i])
    # print(f'#{tc} {ans_list}')
    print(f'#{tc} {len(ans_list)}')