# WorkShop

### 무엇이 중복일까

문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는
duplicated_letters 함수를 작성하시오.

```python
duplicated_letters('apple') # => ['p']
duplicated_letters('banana') # => ['a', 'n']
```

**ans for 1:**

```python
def duplicated_letters(word):
    
    lis_t = []
    ans = []
    for i in range(len(word)):
        if word[i] in lis_t:
            if word[i] in ans:
                pass
            else:
                ans += [word[i]]
        else:
            lis_t += [word[i]]
    return ans
print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
```

```python
# 교수님 답안
def duplicated_letters(word):
    result = []
    for char in word:
        if word.count(char)
    return result

#2
for char in word:
    if word.count(char) >= 2:
		if chat not in result:
    result.append(char)
return result
```



### 소대소대

문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여
반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만
구성된다.

```python
low_and_up('apple') # =>aPpLe
low_and_up('banana')  # => bAnAnA
```

**ans for 2:**

```python
def low_and_up(word):
    ans = ''
    for i in range(len(word)):
        if i == 0:
            ans += word[i].lower()
        elif i % 2 == 1:
            ans += word[i].upper()
        else:
            ans += word[i].lower()
    return ans
print(low_and_up('apple'))
print(low_and_up('banana'))
```

```python
# 교수님 답변
def low_and_up(word):
    result = ''
    for idx in range(len(word)):
        
        result += word[idx]
        
#2
for idx, char in enumerate(word):
    if idx % 2 == 1:
        result += char.upper()
    else:
        result += char.lower()
return result

#3
result = [char.upper() if idx % 2 else char.lower() for idx, char in enumerate(word)]
return ''.join(result) #-> '' 내의 구분자를 기준으로 나눈 후 문자열로 반환
```





### 솔로 천국 만들기

정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

```python
lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]
```

**ans for 3:**

```python
def lonely(numbers):
    for i in range(len(numbers)):
        if i < len(numbers):
            if numbers[i] == numbers[i + 1]:
                numbers.pop(i)
    return numbers
result1 = lonely([1, 1, 3, 3, 0, 1, 1])
result2 = lonely([4, 4, 4, 3, 3])
print(result1) -> [1, 3, 0, 1]
print(result2) -> [4, 4, 3] -> 오답
# 수정
```

```python
# 교수님 답변
def lonely(numbers):
    result = [numbers[0]]
    for number in numbers:
        if result[-1] != number:
            result.append(number)
    return result
```

