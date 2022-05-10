import sys
sys.stdin = open('5099.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 화덕의 크기, M: 피자의 개수
    pizza = list(map(int, input().split())) # 피자의 치즈 분포

    # idx정보와 치즈의 정보를 모두 넣어둔 pizza_idx 리스트를 만들어줌
    # ans = 해당하는 부분의 pizza_idx[i][0] + 1
    pizza_idx = [] # 피자에 대한 정보가 담겨있음

    for aaay in range(len(pizza)):
        pizza_idx.append([aaay, pizza[aaay]])

    pizza_que = [[0, 0] for _ in range(N)] # 화덕, [idx, 치즈]
    # 화덕에 피자를 채워주자
    for i in range(len(pizza_que)):
        pizza_que.append(pizza_idx.pop(0))

    find = 0 # 화덕 내부를 조회하는데 쓰이는 인덱스값
    while len(pizza_que) != 1: # 1개 남을 떄 까지 계속 돌림
        # 소요 시간 절반으로 만들기
        pizza_que[0][1] = pizza_que[0][1] // 2

        # 치즈가 다 녹지 않았다면, 맨 뒤로
        if pizza_que[0][1] != 0:
            pizza_que.append(pizza_que.pop(0))
        # 치즈가 다 녹았다면, 피자를 빼고,
        else:
            pizza_que.pop(0)
            # 남아 있는 피자가 있다면 오븐에 추가
            if len(pizza_idx) != 0:
                pizza_que.append(pizza_idx.pop(0))

    print(f'#{tc} {pizza_que[0][0]+1}')