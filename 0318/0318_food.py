import sys
sys.stdin = open('0318_food.txt')

# 좌표(섞는 음식)가 주어졌을 때, 해당 좌표의 값들의 합을 구하는 함수
def sumfood(a, b):
    taste_list.append(arr[a][b] + arr[b][a])

T = int(input()) # 테스트 케이스의 수
for tc in range(1, T+1):
    N = int(input()) # N*N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    taste_list = []
    # arr[a][b]에 담겨있는 값은 재료 a와 b의 시너지 효과
    # arr[a][b] + arr[b][a] == 맛
    # a == b인 경우는 예외로 해야됨. 카운트 하지 말아야 함
    # 모든 (a, b)쌍에 대하여 맛의 차이가 최소가 되는 (a, b) (aa, bb)를 구해야 함
    # 그때의 최솟값을 찾아내야 함
    # 1. 모든 (a, b)에 대한 맛을 리스트에 저장
    # 2. 오름차순이든 내림차순이든 정렬
    # 3. 0번 인덱스부터 마지막-1 인덱스까지 조회하며 abs(list[i+1] - list[i]) 값을 또다른 리스트에 저장해주자
    # 4. 그 리스트를 오름차순으로 정렬한 후 가장 앞의 값 출력

    for i in range(N):
        for j in range(N):
            if i != j:
                sumfood(i, j)

    find_ans_list = []
    taste_list.sort()
    for z in range(len(taste_list)-1):
        find_ans_list.append(abs(taste_list[z+1]-taste_list[z]))

    find_ans_list.sort()
    ans = find_ans_list[0]
    print(f'#{tc} {ans}')