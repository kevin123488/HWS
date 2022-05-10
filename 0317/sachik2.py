import sys
sys.stdin = open('sachik.txt')

for tc in range(1, 11):
    N = int(input()) # 정점의 수
    arr = [list(input().split()) for _ in range(N)] # 노드와 입력 정보, 연결 정보까지 받아옴
    tree = [0]

    for i in arr:
        tree.append(i)

    k = N
    while k > 0:
        if tree[k][1] == '+':
            tree[k][1] = int(tree[int(tree[k][2])][1]) + int(tree[int(tree[k][3])][1])
        elif tree[k][1] == '-':
            tree[k][1] = int(tree[int(tree[k][2])][1]) - int(tree[int(tree[k][3])][1])
        elif tree[k][1] == '*':
            tree[k][1] = int(tree[int(tree[k][2])][1]) * int(tree[int(tree[k][3])][1])
        elif tree[k][1] == '/':
            tree[k][1] = int(tree[int(tree[k][2])][1]) / int(tree[int(tree[k][3])][1])
        else:
            k -= 1

    ans = int(tree[1][1])
    print(f'#{tc} {ans}')