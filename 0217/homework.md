## Homework

**SWEA 1216**

100 * 100의 평면에서 가장 긴 회문(가로든 세로든)을 찾아 해당 회문의 길이를 출력하는 문제

```python
def palindrome(args):
    if args == args[-1::-1]:
        return True
    else:
        return False

# 최댓값 구하는 함수
def my_max(ar):
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            ar[i], ar[i+1] = ar[i+1], ar[i]
    if ar == []:
        return 0
    else:
        return ar[-1]

for tc in range(1, 11): # 10개의 test case
    tc_num = int(input())
    arr = [list(input()) for _ in range(100)] # 100 * 100의 평면을 받아옴

    # arr에 대해서 arr[0], arr[1], ... , arr[99]까지 조회하며 안에 회문이 있는지 없는지를 확인하고, 만약 회문이 있다면 그 회문의 길이를 리스트에 담아 정렬하여 가장 큰 값을 반환
    # 안에 회문이 있는지 없는지는 어떻게 확인할것인가?

    lis_t = []
    for i in range(100):
        # arr[i]
        for j in range(100):
            for k in range(100):
                if j+k+1 <= 100:
                    if palindrome(arr[i][j:j+k+1]) == True:
                        lis_t += [k+1]

    # 이제 해당 배열을 돌려서 확인해봐야 한다
    # 열 우선순으로 조회해봐야 하기 때문
    real_list = []
    listtttt = []
    for ii in range(100):
        for jj in range(100):
            listtttt += arr[jj][ii]
            if len(listtttt) == 100:
                real_list += [listtttt]
                listtttt = []

    for iii in range(100):
        # real_list[iii]
        for jjj in range(100):
            for kkk in range(100):
                if jjj+kkk+1 <= 100:
                    if palindrome(real_list[iii][jjj:jjj+kkk+1]) == True:
                        lis_t += [kkk+1]
    # 함수화

    ans = my_max(lis_t)
    print(f'#{tc} {ans}')
```

로직

1. 각 행부터 순차적으로 조회해보자.
   - 안에 회문이 있는지 없는지 확인하려면?
   - 시작점의 인덱스값이 0이라고 할 때, 0, 0~1, 0~2 ... 0~99번째 인덱스를 슬라이싱한 값을 모조리 조회해보며 회문인지 아닌지 판별해보자
   - 만약 회문이면, 그 길이를 빈 리스트에 넣어주자
2. 행은 끝났다. 그 다음은?
   - 열 우선 조회를 실시해야 한다.
   - 행 우선 조회와의 가장 큰 차이점은 **'슬라이싱'**의 가능여부
   - 행 우선 조회의 경우 슬라이싱이 가능하지만, 열 우선 조회의 경우 슬라이싱이 안된다
   - 그럼 어떻게 해야 할까?
   - **행렬을 돌려 열 우선조회와 같은 순서로 조회하되, 슬라이싱이 가능하게 해주면 된다**
   - 만약 회문이면, 그 길이를 빈 리스트에 넣어주자
3. 회문의 길이가 담겨있는 리스트를 정렬해 가장 큰 값을 출력해주면 끝