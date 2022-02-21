import sys
sys.stdin = open('2005_input.txt')

# 크기가 N인 파스칼의 삼각형을 만들자
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    memo = [[0]*(N) for _ in range(N)] # memo를 만들자
    # 위의 memo에 값들을 추가해주자
    for i in range(N):
        for j in range(N):
            if j == 0:
                memo[i][j] = 1
            elif i>0 and j>0:
                memo[i][j] = (memo[i-1][j-1] + memo[i-1][j])

    ans_list = []
    for k in range(N):
        ans = memo[k][:k+1]
        ans_list += [ans]

    print(f'#{tc}')

    for z in ans_list:
        for x in z:
            print (x, end=' ')
        print()