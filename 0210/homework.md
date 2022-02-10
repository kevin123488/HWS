## Homework

```python
import sys
sys.stdin = open('1208_input.txt')

# 버블정렬
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

for tc in range(1, 11):
    dump = int(input())
    width_list = list(map(int, input().split()))

    for k in range(dump):
        list_sorted = bubble_sort(width_list)
        list_sorted[-1] -= 1
        list_sorted[0] += 1
        if bubble_sort(list_sorted)[-1] - bubble_sort(list_sorted)[0] == 0 or bubble_sort(list_sorted)[-1] - bubble_sort(list_sorted)[0] == 1:
            print(f'#{tc} {list_sorted[-1] - list_sorted[0]}')
        else:
            pass

    print(f'#{tc} {list_sorted[-1] - list_sorted[0]}')
```

시간이 조금 걸리긴 했지만 내 힘으로 풀었다

처음엔 계속 2씩 적은 값이 출력되길래 '어디서 한번 더 돈거지?'와 같은 생각을 하며 코드를 고쳤다.

코드를 아무리 고쳐봐도 결과값은 바뀌지 않았고...

결국 간단한 테스트 케이스를 만들어 손으로 직접 코드를 하나하나 짚어보게 되었다.

그러다 발견한 오류 -> 최대-최솟값이 1이거나 0이면 값을 출력한 후 break를 걸어 다음 for문을 도는 부분에서 잘못 작성한 부분을 발견했다.

처음엔 list_sorted에 바로 [-1]과 [0]을 붙여 값을 계산해 if문에 넣었다. 그러나 곰곰히 생각해 보니, 해당 if문 위의 코드가 실행됨으로써 더이상 list_sorted[-1]과 list_sorted[0]이 각각 최대, 최솟값이 아닐수도 있겠다는 생각이 들었다.

그래서 if문 돌릴 때 다시 bubble_sort 씌워줬다.

-> 그랬더니 값 제대로 도출됨



## Good