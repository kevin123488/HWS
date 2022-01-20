# WorkShop

### 숫자의 의미

정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

```python
get_secret_word([83, 115, 65, 102, 89]) # => 'SsAfy'
```

**ans for 1:**

```python
def get_secret_word(args):
    l_ist = []
    for i in args:
        a = chr(i)
        # print(type(a))  --> 자료형이 str로 나온다

        l_ist += a   # --> str인 a와 list인 l_ist를 더하는데 값이 나온다..왜지
    sum_of_str = ''
    for k in l_ist:
        sum_of_str += k
    return sum_of_str

result = get_secret_word([83, 115, 65, 102, 89])
print(result)
```

```python
# 다시 작성해본 코드

def get_secret_word(args):
    sum_of_str = ''
    for i in args:
        a = chr(i)
        sum_of_str += a
    return sum_of_str

result = get_secret_word([83, 115, 65, 102, 89])
print(result)
```

```python
# 교수님 답변
def get_secret_word(numbers):
    # 다시 작성해본 코드와 거의 같음
```





### 내 이름은 몇일까? 

문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

```python
get_secret_number('tom') # => 336
```

**ans for 2:**

```python
def get_secret_number(args):
    sum_of_num = 0
    for i in args:
        a = ord(i)
        sum_of_num += a
    return sum_of_num

print(get_secret_number('tom'))
```

```python
# 교수님 답변
def get_secret_number(args):
    result = 0
    for i in args:
        result += ord(i)
    return result

print(get_secret_number('tom'))
```







### 강한 이름

문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```python
get_strong_word('z', 'a') # => 'z'
get_strong_word('tom', 'john') => 'john'
```

**ans for 3:**

```python
def get_strong_word(str1, str2):
    sum_str1 = 0
    sum_str2 = 0
    for i in str1:
        a = ord(i)
        sum_str1 += a
    for k in str2:
        b = ord(k)
        sum_str2 += b
    if sum_str1 > sum_str2:
        return str1
    else:
        return str2

result = get_strong_word('z', 'a')
print(result)
```

```python
# 교수님 답변
def get_strong_word(word1, word2):
    #각 문자열들 아스키 숫자로 변환 후 더할 값
    word1_result = 0
    word2_result = 0
    for i in word1:
        word1_result += ord(i)
    for k in word2:
        word2_result += ord(k)
    
    if word1_result > word2_result:
        return word1
    else:
        return word2
result = get_strong_word('z', 'a')
print(result)

# 값이 같을 때, 비교 불가. 문제 오류임
```

