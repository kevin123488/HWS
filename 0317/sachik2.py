import sys
sys.stdin = open('sachik.txt')

for tc in range(1, 11):
    N = int(input()) # 정점의 수
    arr = [list(input().split()) for _ in range(N)] # 노드와 입력 정보, 연결 정보까지 받아옴
    tree = [0 for __ in range(N+1)]

    for i in arr:
        tree[int(i[0])] = i[1]

    print(tree)