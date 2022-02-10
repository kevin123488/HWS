import sys
sys.stdin = open('googanhap_input.txt')

T = int(input()) # 테스트 케이스의 개수
for tc in range(1, T+1): # 테스트 케이스만큼 순회
    # 정수의 개수 N
    # 구간의 길이 M
    # 개수 N개의 요소를 가지는 리스트 aj
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))

    # 구간합들을 저장할 리스트
    ajj = []

    for k in range(len(aj)-(M-1)):
        # 슬라이싱을 이용할 예정
        # 구간의 길이만큼 슬라이싱 해 해당 요소들의 합을 구하면 됨
        sum_googan = 0
        for z in aj[k:k+M]:
            sum_googan += z
        ajj += [sum_googan]
    # 이제 ajj 리스트의 최댓값과 최솟값을 구해보자
    ajj_min = ajj[:]
    for x in range(len(ajj)-1):
        if ajj[x] >= ajj[x+1]:
            ajj[x], ajj[x+1] = ajj[x+1], ajj[x]

    for y in range(len(ajj_min)-1):
        if ajj_min[y] <= ajj_min[y+1]:
            ajj_min[y], ajj_min[y+1] = ajj_min[y+1], ajj_min[y]

    ans = ajj[-1] - ajj_min[-1]
    print(f'#{tc} {ans}')