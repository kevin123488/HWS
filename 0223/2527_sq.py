import sys
sys.stdin = open('2527.txt')

# 2차원 공간에 두개의 꼭짓점으로 표현되는 직사각형이 있다. 왼쪽 아래의 (x, y), 오른쪽 위의 (p, q)
# 2개의 사각형에 대해 겹침, 접함, 분리됨 총 3가지의 케이스를 가진다
# 즉, 겹치는 부분이 직사각형인지, 선분인지, 점인지, 혹은 없는지를 구분할 수 있다.
# 각 케이스에 대해 직사각형 -> a
# 선분 -> b
# 점 -> c
# 없음 -> d 를 출력하는 코드를 작성해보자

for i in range(1, 5):
    point_list = list(map(int, input().split())) # x1, y1, p1, q1, x2, y2, p2, q2
    # 첫번째 사각형에 대해, x1이 열 인덱스, y1이 행 인덱스, p1이 열 인덱스, q1이 행 인덱스
    # 이차원 리스트에 해당 사각형들을 그려보자
    N = max(point_list)
    arr = [[0] * (N+1) for _ in range(N+1)] # 사각형을 그릴 평면을 받아옴

    # 첫번째 사각형
    for sero in range(N+1):
        for garo in range(N+1):
            if point_list[1] <= sero <= point_list[3] and point_list[0] <= garo <= point_list[2]:
                arr[sero][garo] += 1

    # 두번째 사각형
    check_list = []
    for s_ero in range(N+1):
        for g_aro in range(N+1):
            if point_list[5] <= s_ero <= point_list[7] and point_list[4] <= g_aro <= point_list[6]:
                if arr[s_ero][g_aro] == 1:
                    arr[s_ero][g_aro] += 1
                    check_list += [[s_ero, g_aro]]

    # check_list의 길이가 0이다 -> d 출력
    # 길이가 1이다 -> c 출력
    # 직사각형인지, 선분인지 판별은? 어떻게?
    find_i = []
    find_j = []
    if len(check_list) == 0:
        print('d')
    elif len(check_list) == 1:
        print('c')
    else:
        for z in check_list:
            find_i += [z[0]]
            find_j += [z[1]]
        if len(set(find_i)) == 1 or len(set(find_j)) == 1:
            print('b')
        else:
            print('a')