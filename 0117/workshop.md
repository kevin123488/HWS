![image-20220117220702861](workshop.assets/image-20220117220702861.png)

**ans for 1:**

```python
a = int(input())
for i in range(1, a + 1):
	print(i)
```









![image-20220117220929318](workshop.assets/image-20220117220929318.png)

**ans for 2:**

```python
a = int(input())
for i in range(a, -1, -1):
	print(i)
```

```python
number = int(input())
for i in range(number, -1, -1):
    print(i)
```







![image-20220117221301132](workshop.assets/image-20220117221301132.png)

**ans for 3:**

```python
a = int(input())
ans = 0
for i in range(a + 1):
	ans = ans + i
print(ans)
```

```python
# 값 입력받기
number = int(input())

# 출력 할 최종값
result = 0
for i in range(1, number + 1):
    result += i

print(result)

# print(sum(range(1, number + 1)))
# 위의 방법도 가능하지만, 당분간은 built in function(내장함수) 사용 금지
```

