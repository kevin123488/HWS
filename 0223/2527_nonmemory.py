import sys
sys.stdin = open('2527.txt')

for i in range(1, 5):
    point_list = list(map(int, input().split())) # x1, y1, p1, q1, x2, y2, p2, q2
    # 첫 사각형: (x1, y1), (p1, q1)으로 구성된 사각형
    # 두번째 사각형: (x2, y2), (p2, q2)로 구성된 사각형
    # 첫 풀이땐 N*N 이차원 리스트를 받아온 후 해당 영역에 1씩 더해줌으로써 겹치는 구간을 찾아냈다. -> 메모리 초과
    # tc중 겁나 구간이 넓은게 있나보다. 그럼 다른 방법을 찾아봐야지...
    # 첫 사각형의 좌우하상의 절편은?
    sq1_x1 = point_list[0]
    sq1_x2 = point_list[2]
    sq1_y1 = point_list[1]
    sq1_y2 = point_list[3]

    # 두번째 사각형의 좌우하상의 절편은?
    sq2_x1 = point_list[4]
    sq2_x2 = point_list[6]
    sq2_y1 = point_list[5]
    sq2_y2 = point_list[7]

    # 1. a

    if sq1_x1 == sq2_x2 or sq1_x2 == sq2_x1 or sq1_y1 == sq2_x2 or sq1_y2 == sq2_y1:
        print('b')
    elif sq1_x1 == sq2_x2 and sq1_y1 == sq2_y2 or sq1_x2 == sq2_x1 and sq1_y1 == sq2_y2 or sq1_x1 == sq2_x2 and sq1_y2 == sq2_y1 or sq1_x2 == sq2_x1 and sq1_y2 == sq2_y1:
        print('c')
    elif sq1_x1 < sq2_x1 < sq1_x2 or sq1_x1 < sq2_x2 < sq1_x2 or sq1_y1 < sq2_y1 < sq1_y2 or sq1_y1 < sq2_y2 < sq1_y2:
        print('a')
    else:
        print('d')