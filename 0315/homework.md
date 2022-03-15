## 0315 HW

```python
# 로직 정리
# 1. 시작점은 s, 도착점은 a
# 2. s에서 탐색을 실시. 지나온 곳은 arr에 1 표기하기
# 3. 탐색중 2개 이상의 갈림길이 나오면? stack에 해당 좌표 넣은 후 계속 탐색
# 4. 탐색하다 막히면? stack[-1]로 돌아간 후 다시 탐색 (지나온 길은 1로 표시되어 있을 것이므로 이미 간 곳으로는(실패한 경로) 탐색하지 않을것)
# 5. s == a가 되는 순간 1 반환
# 6. s != a 이며 더 이상 탐색할 곳이 없는데 stack이 비어있는 순간 0 반환

import sys
sys.stdin = open('miro.txt')

# 탐색 가능 갈래의 수를 확인하는 함수
def check(s):
    di = [1, 0, -1, 0]  # 우하좌상
    dj = [0, 1, 0, -1]  # 우하좌상
    cnt = 0
    for i in range(4):
        b = s[0]
        c = s[1]
        b = s[0] + di[i]
        c = s[1] + dj[i]
        if 0 <= b <= 16 and 0 <= c <= 16 and arr[b][c] == 0:
            cnt += 1
    if cnt > 1:
        stack.append(s)
    return cnt

# 델타탐색 함수
def delta(arr, s):
    # s는 시작 좌표
    global a
    global stack
    di = [1, 0, -1, 0] # 우하좌상
    dj = [0, 1, 0, -1] # 우하좌상
    # 1. 갈 수 있는 곳 확인
    if s == a:
        return 1
    elif check(s) == 0:
        if stack == []:
            return 0
        else:
            s = stack[-1]
            delta(arr, s)
    else:
        for i in range(4):
            b = s[0]
            c = s[1]
            b = s[0] + di[i]
            c = s[1] + dj[i]
            if 0 <= b <= 16 and 0 <= c <= 16 and arr[b][c] == 0:
                arr[s[0]][s[1]] = 1
                s = [b, c]
                delta(arr, s)

for tc in range(1, 11):
    tc_1 = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    stack = []
    # 시작 좌표와 도착 좌표를 만들자
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                s = [i, j]
            elif arr[i][j] == 3:
                a = [i, j]
    # s: 시작좌표, a: 도착좌표
    print(f'#{tc} {delta(arr, s)}')
```

result : 재귀에러

.

.

.

보통 dfs 문제를 풀 땐 visited 리스트를 만들어 이동한 부분에 방문체크를 해주는 방식으로 진행한다.

평소 접해온 방식대로 풀어볼까 하다, '방문체크 할 필요없이 여러갈래인 좌표를 stack에 넣어준 다음 막히면 거기로 돌아가는 방식으로 가면 안되나?' 같은 생각에 빠지게 되었고, 그 결과 난잡한 코드를 짜고 말았다

흠... dfs, bfs... 아직 잘 모르겠다.