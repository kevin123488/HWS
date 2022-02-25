## Homework

```python
def cycle(arr):
    i = 1
    while i < 6:
        a = arr.pop(0) # 가장 앞의 값을 뽑아낸 후 a에 담기
        if a - i <= 0: # 만약 가장 앞의 값에서 i를 뺀 값이 음수라면?
            arr.append(0) # arr에 -1이라는 값을 append 해줌
            break # 그리고 종료조건에 다다랐으므로 break
        else: # 그 외의 경우
            arr.append(a-i) # 계산한 결과를 append 해줌
        i += 1
    return

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 받은 arr를 cycle 돌린 후 결과를 출력하자
    while True:
        cycle(arr) # cycle 함수를 계속 돌려보자
        # 종료조건을 설정해야 한다
        if 0 in arr:
            break # cycle을 돌고 난 후 arr에 0이 포함되어있다면 break하고 결과 내기

    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
```

암호가 될 리스트의 요소가 0이 되거나 0보다 낮은 값이 되는 순간 종료를 해준 후 결과를 출력하면 되는 문제

였으나... 문제를 잘못 봐서 '0일땐 ok이고 음수값이 나올때 0으로 바꿔주며 해당 코드를 종료시켜야 한다'라고 이해해버림... 그 결과 꽤 긴 시간동안 '10개의 테스트 케이스중 4개가 맞았습니다'를 벗어나지 못했고... 결국... 12시가 넘어서야 겨우겨우 제출하게 되었다.

하... 집중하자