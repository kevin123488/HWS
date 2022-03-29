# 화물 도크
import sys
sys.stdin = open('input_5202.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 작업시간 s와 종료시간 e를 [s, e]의 형태로 담아 이차원리스트

    find_list = []
    for i in range(len(arr)):
        k = arr[i][1]-arr[i][0] # 작업시간
        find_list.append([k, i]) # 작업시간과 인덱스를 find_list에 넣어준다

    i = 1
    while len(find_list)-i != 0:
        for k in range(len(find_list)-i):
            if find_list[k][0] > find_list[k+1][0]: # 작업시간이 큰 애를 뒤로 보내주자
                find_list[k],find_list[k+1] = find_list[k+1], find_list[k]
        i += 1

    # 위의 과정을 통해 find_list는 작업시간을 기준으로 오름차순 정렬 되었다
    # 작업시간의 겹침을 판별하자
    # find_list에 담긴 순으로(작업시간이 적은 순으로) 실행해보자
    # 우선 가장 앞의 값을 넣고, 그 다음값을 넣을 때 겹침유무를 판다하자. 겹친다면? 다음 값으로 넘어가자. 겹치지 않는다면? 값을 ans_list에
    # 넣어주고 다음 값으로 넘어가자.

    # print(f'#{tc} {find_list}')
    ans_list = [find_list[0]] # 겹치지 않는 값을 넣어줄 리스트
    # for z in range(len(find_list)-1): find_list를 조회하며
    for z in range(1, N-1):
        if arr[ans_list[-1][1]][1] <= arr[find_list[z+1][1]][0] or arr[ans_list[-1][1]][0] >= arr[find_list[z+1][1]][1]: # 겹치지 않을 때
            ans_list.append(find_list[z])

    print(f'#{tc} {ans_list}')