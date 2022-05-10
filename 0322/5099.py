# 피자 굽기
# 한번에 N개의 피자를 구울 수 있는 화덕
# 1번부터 M번까지의 피자를 순차적으로 넣지만, 치즈의 양이 제각각 이므로 꺼내는 순서는 넣는 순서와 다를 수 있음
# 1번부터 N번까지 일단 넣음
# 걔네 돌려가면서 치즈 확인함. 다음번 확인 때 해당 피자의 치즈는 치즈//2가 됨
# 치즈의 양이 0이 되면 꺼냄
# 꺼낸 자리에 새 피자 넣음
# 화덕에 제일 마지막까지 남아있는 피자는?

import sys
sys.stdin = open('5099.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 화덕의 크기, M: 피자의 개수
    pizza = list(map(int, input().split())) # 피자의 치즈 분포

    # idx정보와 치즈의 정보를 모두 넣어둔 pizza_idx 리스트를 만들어줌
    pizza_idx = []
    for aaay in range(len(pizza)):
        pizza_idx.append([aaay, pizza[aaay]])


    hwa_duk = [[0, 0] for _ in range(N)] # N개의 피자가 들어갈 수 있는 화덕. [idx, 치즈]
    for i in range(N):
        hwa_duk[i] = pizza_idx.pop(0) # 일단 1번부터 N번까지 넣음

    # print(f'#{tc} {hwa_duk}')
    find = 0
    while len(hwa_duk) != 1:
        cnt = 0
        if hwa_duk[find][1] == 0:
            if pizza_idx[0]:
                hwa_duk[find] = pizza_idx.pop(0)
        else:
            hwa_duk[find][1] = hwa_duk[find][1]//2
        find += 1
        find = find % N
        for k in hwa_duk:
            if k[1] != 0:
                cnt += 1
        if cnt == 1:
            break

    for kk in hwa_duk:
        if kk[1] != 0:
            ans = kk[0] + 1

    print(f'#{tc} {ans}')