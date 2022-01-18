![image-20220118110016048](02_workshop.assets/image-20220118110016048.png)

**ans for 1:**

```python
N = int(input())
for i in range(1, N + 1):
	if N%i == 0:
		print(i)
	else:
		continue
```

![image-20220118110058849](02_workshop.assets/image-20220118110058849.png)

**ans for 2:**

```python
numbers = [
	85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 
	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
	52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
numbers.sort()

a = len(numbers)

if a%2 == 0:
	print('중간값 없음')
else:
	print(numbers[a//2])
```

![image-20220118110123724](02_workshop.assets/image-20220118110123724.png)

**ans for 3:**

```python
a = int(input())
for i in range(1, a+1):
	for k in range(1, i+1):
		print(k)
# 미완코드
```

