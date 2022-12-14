## workshop

**1. 평균 점수 구하기**

**key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.**

```python
get_dict_avg({
    'python' : 80,
    'algorithm': 90,
    'django': 89,
    'web': 83,
}) #=> 85.5
```

**ans for 1:**

```python
def get_dict_avg(args):
    su_m = 0
    count = 0
    for i in args:
        su_m += args[i]
        count += 1
    return su_m/count

result = get_dict_avg({
    'python' : 80,
    'algorithm': 90,
    'django': 89,
    'web': 83,
})
print(result)
```

```python
# 교수님 답변
def get_dict_avg(scores):
    return sum(scores.values()) / len(scores.keys())
```





**2. 혈액형 분류하기**

**여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.**

```python
count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
])
```

**ans for 2:**

```python
def count_blood(args):
    a_count = 0
    b_count = 0
    ab_count = 0
    o_count = 0
    for i in args:
        if i == 'A':
            a_count += 1
        elif i == 'B':
            b_count += 1
        elif i == 'AB':
            ab_count += 1
        else:
            o_count += 1
    return dict(A = a_count, B = b_count, AB = ab_count, O = o_count)

result = count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
])

print(result)
```

```python
# 교수님 답변
def count_blood(blood):
    # 안에 있는 각 값들에 해당하는
    # 키를 가진 딕셔너리를 만들고
    # 그 키에 해당하는 값들을 채워 나가야 한다
    result = {}
    # 전체 리스트 반복문 돌려서
    for val in blood:
        # 만약 result에 해당하는 키값이 있다면 +1
        if result.get(val):
            result[val] += 1
        else:
            result[val] = 1
    return result

# 2
result = {}
for key in blood:
    result[key] = result.get(key, 0) + 1
return result
```

