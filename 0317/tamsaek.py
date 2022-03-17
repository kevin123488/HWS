# swea 5176

import sys
sys.stdin = open('tamsaek.txt')

# N이 주어졌을 때, 해당 이진트리의 루트와 N//2번 노드의 값을 출력하시오

def treetree(v, N):
    global cnt
    if v <= N:
        treetree(2*v, N) # 왼쪽 자식 노드는 부모 노드 인덱스의 2배가 되는 인덱스를 가진다
        tree[v] = cnt # 해당하는 인덱스에 cnt값을 넣어줌. 넣어주고 난 후 cnt를 1 증가시켜야 함
        cnt += 1
        treetree(2*v+1, N) # 왼쪽 넣어줬으니 이제 오른쪽 넣어줄 차례

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1 # 노드 1부터 시작
    treetree(1, N)

    print(f'#{tc} {tree[1]} {tree[N//2]}')