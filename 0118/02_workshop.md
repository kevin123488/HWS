![image-20220118110016048](02_workshop.assets/image-20220118110016048.png)

**ans for 1:**

```python
N = int(input())
for i in range(1, N + 1):
	if N%i == 0:
		print(i, end='')
	else:
		continue
```

```python
# 교수님 답변
N = int(input())
for i in range(1, N + 1):
    if N%i == 0:
        print(i, end='')# 원래면 값이 세로로 주르륵 나옴. end = ''을 써주면 값 나오고 공백 후 '옆'에 다음 값이 지정됨. 파이썬 공식문서-print함수 파트 확인.
#기본적으로 print함수는 end ='\n'으로 줄바꿈을 디폴트로 가짐. 그러나 end=''를 넣어주면? 디폴트(줄바꿈)값 대신 쭉 쓰는걸로 바뀜.
    else:
        
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

```python
sort 없이 정렬하는 법.
numbers = [5, 2, 3, 1, 4]
#for i in range(len(numbers)):
    #for j in range(i + 1, len(numbers)):
```

```python
# 교수님 답변
sorted_numbers = sorted(numbers)
length = 0
for i in numbers:
    length += 1
center = length//2
print(sorted_numbers[center])
```





![image-20220118110123724](02_workshop.assets/image-20220118110123724.png)

**ans for 3:**

```python
a = int(input())
for i in range(1, a+1):
	for k in range(1, i+1):
		print(k, end='')
    print()
```

