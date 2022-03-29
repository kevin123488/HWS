## 0329 HW

```python
# 베이비진 게임

# run인지 triple인지 아무것도 아닌지 판별해주는 함수
def de_fine_tri(arr): # arr를 입력받아 해당 arr의 점수를 판단
    for i in range(len(arr)):
        if arr.count(arr[i]) >= 3:
            return 1
    return 0

def de_fine_run(arr):
    for i in range(len(arr)):
        if arr[i]-1 in arr and arr[i]+1 in arr:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 0부터 9까지의 숫자카드 4세트를 섞은 후 6장을 뽑자
    # 연속인 숫자가 3개 이상 -> run
    # 같은 숫자가 3개 이상 -> triple
    # 게임 시작하면 p1과 p2가 1장씩 카드를 가져감
    # 먼저 run이나 triple을 달성하는 사람이 이김

    p1 = [] # player 1이 가져가는 카드
    p2 = [] # player 2가 가져가는 카드
    for i in range(6):
        p1.append(arr[i*2])
        p2.append(arr[i*2+1])
        if len(p1) >= 3: # 3장 이상의 카드를 배부받았을 때
            if de_fine_run(p1) or de_fine_tri(p1): # p1이 걸렸는데
                if de_fine_run(p2) == 0 and de_fine_tri(p2) == 0: # p2가 run, tri 둘 다 아니라면?
                    print(f'#{tc} 1') # p1이 이긴거니까 1 출력
                    break
                else: # p2에게도 run이나 tri중 걸린게 있다면
                    print(f'#{tc} 1') # 둘 다 동시에 걸린거면 1번이 이김(밸런스 패치 시급)
                    break
            elif de_fine_run(p2) or de_fine_tri(p2): # 만약 p1이 안걸렸는데 p2가 걸렸다면?
                print(f'#{tc} 2') # p2가 이긴거니까 2 출력
                break
        if len(p1) == 6: # 다 뽑았을 때
            print(f'#{tc} 0')
```

로직은 다음과 같다.

1. player 1의 리스트와 player 2의 리스트를 만들어준다
2. 리스트에 값을 하나씩 넣어주다 player 1의 리스트의 길이가 3이 되는 순간부터 판별을 시작한다
3. 만약 p1이 run이거나 tri면? -> 1번이 이겼음
   - 어째서?-> p1이 p2와 동시에 조건을 달성할 경우, p1의 승리로 책정됨
4. 만약 p1이 run과 tri 둘 다 아니라면?
   - p2 확인해보고 p2가 만족-> p2의 승리로 책정
   - p2 확인해보고 p2가 불만족-> p1, p2리스트에 하나씩 추가
5. 다 뽑았는데 아직 만족한게 없다면? -> 무승부



## 선공망겜