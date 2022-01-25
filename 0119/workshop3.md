## Workshop3

1. **List의 합 구하기**
**정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.**

```python
list_sum([1, 2, 3, 4, 5]) #=> 15
```

**ans for 1:**

```python
def list_sum(args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum

result = list_sum([1, 2, 3, 4, 5])
print(result)
```

**parameter에 *args 넣으면 실행 안됨. 이유는?**

```python
# 교수님 답변
def list_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
```





2. **Dictionary로 이루어진 List의 합 구하기**
**Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.**

```python
dict_list_sum([{'name': 'kim', 'age': 12, 'name': 'lee', 'age': 4}]) #=> 16
```

**ans for 2:**

```python
def dict_list_sum(args):
    sum = 0
    count = 0
    for i in args[0]:
        if i == 'age':
            sum += args[0][count]
            count += 1
        else:
            count += 1
    return sum

result = dict_list_sum([{'name': 'kim', 'age': 12, 'name': 'lee', 'age': 4}])
print(result)

# 위의 코드를 실행하면 keyerror가 뜬다. 중복된 age들중 끝부분의 age를 제외하고 삭제되어 key를 찾을 수 없게 된걸까? 모르겠다...

# 문제를 잘못 썻다.
```

```python
# 교수님 답변

```







3. **2차원 List의 전체 합 구하기**
**정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.**

```python
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=> 55
```

**ans for 3:**

```python
def all_list_sum(args):
    sum = 0
    for i in args:
        for k in i:
            sum += k
    return sum

result = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(result)
```

```py
# 신기한거
print(sum([1], [2, 3], []))
# sum의 디폴트값은 변수 + 0. []을 추가해줌으로
# 디폴트 0을 []으로 바꿈.
print(*sum([1], [2, 3], [])) 하면 언패킹까지 ㄱㄴ.
-> 1 2 3
```

