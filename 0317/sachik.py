import sys
sys.stdin = open('sachik.txt')

for tc in range(1, 11):
    N = int(input()) # 정점의 총 수
    tree = [0]
    for i in range(N):
        arr = list(input().split())
        tree.append(arr[1])

    # tree에 값을 넣어뒀음
    # 역으로 조회하면서 계산해보자
    k = N
    while k > 1:
        if tree[k//2] == '+':
            tree[k//2] = int(tree[(k//2)*2]) + int(tree[(k//2)*2+1])
        elif tree[k//2] == '-':
            tree[k//2] = int(tree[(k//2)*2]) - int(tree[(k//2)*2+1])
        elif tree[k // 2] == '*':
            tree[k//2] = int(tree[(k//2)*2]) * int(tree[(k//2)*2+1])
        elif tree[k // 2] == '/':
            tree[k//2] = int(tree[(k//2)*2]) / int(tree[(k//2)*2+1])
        else:
            k -= 1

    ans = round(tree[1])
    print(f'#{tc} {ans}')