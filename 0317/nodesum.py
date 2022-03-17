# swea 5178
import sys
sys.stdin = open('nodesum.txt')
# 완전 이진 트리
# 리프의 값을 제외하면, 노드들엔 자식 노드들의 값의 합이 들어있다

# 후위탐색
def post(v):
    if v<=N:
        post(v*2)
        post(v*2+1)
        if (v//2)*2+1 <= N:
            tree[v//2] = tree[(v//2)*2] + tree[(v//2)*2+1]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N: 노드의 수, M: 리프 노드의 수, L: 출력할 노드
    arr = [list(map(int, input().split())) for _ in range(M)] # 리프노드의 번호와 저장된 값을 받아옴

    tree = [0 for __ in range(N+1)] # 노드 번호와 해당하는 값을 넣어줄 것 # 노드 번호는 인덱스가 말해주므로, 값만 넣자
    for i in range(len(arr)):
        if tree[arr[i][0]] == 0:
            tree[arr[i][0]] = arr[i][1]
    # tree의 인덱스: 리프노드의 번호, 해당 인덱스에 들어있는 값: 리프노드의 값
    # 탐색을 시작할 노드 번호: 1
    if N%2 == 0:
        tree[N//2] = tree[N]
    post(1)
    print(f'#{tc} {tree[L]}')