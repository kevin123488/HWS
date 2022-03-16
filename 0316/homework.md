## Tree 과제

```python
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
```

오늘 배운 tree를 이용한 문제.

사실 아직 tree의 개념이 머릿속을 둥둥 떠다니는 기분이다.



이 tree라는 개념을 응용하기 위해선 사실 **받아오는 데이터를 원하는 형태의 tree**로 정제하는 행위가 가장 중요한 것 같다.

위 문제의 경우 

```html
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
```



이런 식으로 데이터를 받아오는데, 각 행의 첫번째 값은 parent의 번호이고 두번째 값은 출력해야하는 값이다.

tree를 `tree = [[0, 0] for _ in range(N+1)]`으로 설정해준다. N+1로 설정해주는 이유는 노드의 번호와 노드의 인덱스를 맞춰주기 위함이다. 즉, 1번 노드(처음 조회를 시작하는 노드)를 tree의 1번 인덱스에 넣어주기 위함이라는 뜻이다.



해당 트리를 조회하며 parent값에 해당하는 인덱스의 [0, 0]을 찾아 child의 인덱스값을 넣어준다. 그 후 child의 인덱스값을 바탕으로 inorder함수를 돌려주면 중위순회 완료-