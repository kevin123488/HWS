# 0318_food.py 오답원인
# 식재료가 4개 있다 치면(a, b, c, d), (a, b)를 이용해 첫 요리를 만들었을 경우 다음 요리는(c, d)를 이용하여 만들어야 한다는 것을
# 간과한 채 (a, b) ~ (a, d) ~ (c, d)까지 모든 경우의 수를 이용해 답을 구했다.
# 앞의 코드에 추가해줘야 할 점:
# 첫 좌푯값(a, b)을 잡았으면 다음 좌푯값은 이용하지 않은 식재료를 이용하는 방향으로 잡아야 한다.
# 즉, 순열과 조합을 이용해야 한다
# 어떻게 짜더라?
# 직접 만들어보자
# 짜고 난 후 해당 식재료들의 좌표쌍이 들어있는 이차원 리스트를 만들고
# 그 리스트의 값들을 앞서 만든 sumfood() 함수에 넣어 이하생략하면 답이 나올 듯 하다

import sys
sys.stdin = open('0318_food.txt')

def taste_sum(a, b):
    return arr[a][b] + arr[b][a]

def howtosolve():
    for z in ans_list:
        taste_list.append(taste_sum(z[0], z[1]))
        for ii in range(N):
            for jj in range(N):
                if ii not in z and jj not in z and ii < jj:
                    taste_list.append(taste_sum(ii, jj))

T = int(input()) # 테스트 케이스의 수
for tc in range(1, T+1):
    N = int(input()) # N*N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans_list = []
    for i in range(N):
        for j in range(N):
            if i != j and i < j:
                ans_list.append([i, j])

    # ans_list에 시작점의 좌표를 잡아뒀음
    
    taste_list = []

    howtosolve()
    taste_list.sort()
    real_taste_list = []
    for taste in range(len(taste_list)):
        if taste%2:
            real_taste_list.append(taste_list[taste])

    ansfind_list = []
    for k in range(len(real_taste_list)-1):
        ansfind_list.append(real_taste_list[k+1]-real_taste_list[k])

    ansfind_list.sort()
    ans = ansfind_list[0]

    print(ans)