# 피자굽기

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
        # if pizza_que[find][1] == 0: # 치즈 다 녹았으면
        #     if pizza_idx: # 남은 피자가 있으면
        #         pizza_que.pop(find)  # 그 피자 빼주고
        #         pizza_que.append(pizza_idx.pop(0)) # pizza_idx에서 순서대로 넣어줌
        #     else: # 남은 피자가 없으면
        #         pizza_que.pop(find)
        # else:
        #     pizza_que[find][1] = pizza_que[find][1]//2
        #     pizza_que.append(pizza_que.pop(find))
        # find = find % N
        # 만약 화덕에 [0, 0] 여러개와 그 외의 것 하나만 있다면? break
    # -----------------------윗부분은 줄여놓고 확인 안하고 돌리는 로직. 한번 더 돌아야 됨----------------------------
        pizza_que[find][1] = pizza_que[find][1]//2 # 일단 조회중인 피자는 절반 줄여두고 봐야됨
        if pizza_que[find][1] == 0: # 치즈 다 녹았으면?
            pizza_que.pop(find)
            if pizza_idx: # 아직 화덕에 넣지 않은 피자가 있을 경우
                pizza_que.append(pizza_idx.pop(0))
        else: # 치즈가 다 녹지 않았다면?
            pizza_que.append(pizza_que.pop(find))

    ans = pizza_que[0][0] + 1
    print(f'#{tc} {ans}')