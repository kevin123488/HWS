# 화물 도크
import sys
sys.stdin = open('input_5202.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 화물의 이용 시간 정보를 담아둠
    # 제일 이른 시간부터 투입시키자

    i = 1
    while len(arr) - i != 0:
        for k in range(len(arr) - i):
            if arr[k][0] > arr[k + 1][0]:  # 시작시간이 늦은 애를 뒤로 보내주자
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
        i += 1

    # 이제 작업시간이 이른 친구들부터 넣어주면 된다
    ans_list = [arr[0]]
    for i in range(1, N):
        if arr[i][0] < ans_list[-1][1]: # 시간이 겹침
            continue
        else: # 시간이 겹치지 않음
            ans_list.append(arr[i])

    print(f'#{tc} {len(ans_list)}')