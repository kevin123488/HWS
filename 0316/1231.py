# 중위순회
# 트리는 완전이진트리
# 노드당 하나의 알파벳

def inorder(v):
    if v:
        inorder(tree[v][0])
        print(tree[v][-1], end='')
        inorder(tree[v][1])

import sys
sys.stdin = open('1231.txt')

for tc in range(1, 11):
    N = int(input()) # 정점의 개수
    arr = [list(input().split()) for _ in range(N)]

    # tree 생성
    tree = [[0, 0] for _ in range(N+1)] # 노드의 개수보다 1 많게 해야됨 # 부모의 값과 인덱스를 맞추고, [0, 0] 안엔 자식 1, 2 ㄱ
    # 인덱스 맞춰줘야 되므로(0이아닌 1부터 시작)
    last = 1
    # 1 [['1', 'W', '2', '3'], ['2', 'F', '4', '5'], ['3', 'R', '6', '7'], ['4', 'O','8'], ['5', 'T'], ['6', 'A'], ['7', 'E'], ['8', 'S']]
    for z in range(len(arr)):
        parent = int(arr[z][0])
        tree[parent].append(arr[z][1])
        if tree[parent][0] == 0:
            if len(arr[z]) >= 3:
                tree[parent][0] = int(arr[z][2])
                if len(arr[z]) == 4:
                    tree[parent][1] = int(arr[z][3])
    # tree에 정보를 저장했다

    print(f'#{tc} ', end='')
    inorder(1)
    print()