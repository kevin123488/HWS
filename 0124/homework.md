## Homework

**1. 모음은 몇 개나 있을까?**

**문자열을 전달받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오. 단, count() 메서드를 활용하여 작성하시오.**

```python
count_vowels('apple') #=> 2
count_vowels('banana') #=> 3
```

**ans for 1:**

```python
def count_vowels(args):
    return args.count('i')+args.count('a')+args.count('e')+args.count('o')+args.count('u')
result1 = count_vowels('apple')
result2 = count_vowels('banana')
print(result1, result2)
```

```python
# 교수님 답안
def count_vowels():
    # 모음이 무엇인지 파악
    vowels = 'aeiou'
    # 최종 반환할 값
    result = 0
    # word 파라미터에 모음이 몇개인지 파악해야 함
    # count 메서드 -> count(x) x의 개수를 세어준다
    # 반복문은?
    for vowel in vowels:
        # 특정 모음 'a'.. 등이 word에 몇 개 있는지 세기 ㄱ
        result += word.count(vowel)
    return result
```





**2. 문자열 조작**

**다음 중, 문자열(string)를 조작하는 방법으로 옳지 않은 것을 고르시오.**

```python
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다. # .index(x)는 없으면 오류 반환
(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를
기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면
공백을 기준으로 나눈다.
(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로
바꿔서 반환한다.
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를
찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.
```

**ans for 2:**

```python
(4), 특정 문자를 지정하지 않으면, 양쪽의 공백을 제거한다.
```





**3. 정사각형만 만들기**

**각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.**

```python
only_square_area([32, 55, 63], [13, 32, 40, 55])
#=> [1024, 3025]
```

**ans for 3:**

```python
def only_square_area(a, b):
    lis_t = []
    for i in range(len(a)):
        if a[i] in b:
            lis_t += [a[i]**2]
    return lis_t

result = only_square_area([32, 55, 63], [13, 32, 40, 55])
print(result)
```

```python
# 교수님 답안
def only_square_area(widths, heights):
    result = []
    for width in widths:
        for height in heights:
            if width == height:
                result.append(width * height)
    return result 

# 답안 2
# 리스트 컴프리헨션
# 리스트에 최종적으로 추가할 값 + 반복문 순서대로
result = [width * height for width in widths for height in heights if width == height]

# 답안 3
# 두 리스트를 비교해서 중복되는 값만 찾으면 됨
value = set(widths) & set(heights)
result = []
for val in value:
    result.append(val**2)
return result

#
return [val**2 for val in set(widths) & set(heights)]
```

