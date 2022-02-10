import sys
sys.stdin = open('bus_input.txt')

T = int(input()) # 노선의 개수 받아옴. 노선의 수 만큼 K, N, M쌍이 나타남
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 한번 충전 후 최대로 이동할 수 있는 정류장 K
    # 0번 정류장부터 N번 정류장까지
    # 충전기가 설치된 M개의 정류장

    # N의 값 -> 0 부터 N 까지의 정류장이 만들어짐
    choong_jeun_list = list(map(int, input().split())) # 충전시설의 위치를 받아옴
    count = 0 # 몇회 이동해야 하는지 저장할 변수
    N_list = [0] * (N+1) # 버스 정류장을 표현할 리스트

    # K만큼 일단 가고, 거기 충전소 있으면 충전하고, 없으면 가장 가까이 있는 충전소로 가는 방식으로 진행하면?
    for i in choong_jeun_list:
        N_list[i] += 1

    for k in range(len(N_list)):
        if N_list[k] == 1:
            if k == K:
                count += 1
    print(count)