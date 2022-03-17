import sys
sys.stdin = open('heapheap.txt')
# 이진 최소힙을 이용하자

def plus(idx):
    global ans
    if idx > 1:
        ans += tree[idx]
        idx = idx // 2
        plus(idx)
    else:
        ans += tree[idx]
        return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    last = 1
    tree = [0 for _ in range(N+1)]
    for i in range(len(arr)):
        if not tree[last]:
            tree[last] = arr[i]
        else:
            last += 1
            child = last
            parent = child // 2

            tree[child] = arr[i]
            while tree[parent] > tree[child]:
                tree[parent], tree[child] = tree[child], tree[parent]
                child = parent
                parent = parent // 2

    # 마지막 노드의 조상들의 합을 구하자
    idx = tree.index(tree[-1]) # 마지막 노드의 인덱스를 받아오자
    first_ans = tree[idx]
    ans = 0
    plus(idx)
    real_ans = ans - first_ans
    print(f'#{tc} {real_ans}')