# 연습문제1 순회
'''
첫 줄에는 정점의 총 수 V가 주어짐. 그 다음 줄에는 V-1게의 간선.
전위순회의 순서대로 노드를 출력하라.
'''
import sys
sys.stdin = open('p1_input.txt')

def pre(node): # 전위 순회
    if node:
        print(f'{node}', end=' ')
        pre(tree[node][0]) # 해당노드의 왼쪽 조사
        pre(tree[node][1]) # 해당노드의 오른쪽 조사

def in_(node): # 중위 순회
    if node:
        in_(tree[node][0])  # 해당노드의 왼쪽 조사
        print(f'{node}', end=' ')
        in_(tree[node][1]) # 해당노드의 오른쪽 조사

def post(node): # 후위 순회
    if node:
        post(tree[node][0])  # 해당노드의 왼쪽 조사
        post(tree[node][1]) # 해당노드의 오른쪽 조사
        print(f'{node}', end=' ')

V = int(input()) # 각 노드의 수
E = V-1 # 간선의 수
arr = list(map(int, input().split())) # 간선 정보

'''
1번 노드
왼쪽: 2번
오른쪽: 3번
부모: 없음

2번 노드
왼쪽: 4번
오른쪽: 없음
부모: 1번

3번 노드
왼쪽: 5번
오른쪽: 6번
부모: 1번
'''

# 어떻게 간선의 정보를 정제할 것인가? 2차원 리스트로 해보자
tree = [[0, 0, 0] for _ in range(V+1)] # 0번은 이용하지 않기 때문
# [ch1, ch2, 부모]의 형태로 넣어줄 것
# 간선의 개수만큼 반복
for i in range(E):
    parent, child = arr[i*2], arr[i*2+1]
    # print(parent, child)
    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent
    # print(tree)

# 시작할 노드 번호를 넣어준다
pre(1)
print()
in_(1)
print()
post(1)