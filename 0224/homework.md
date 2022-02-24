## Homework

후위계산식을 만들어 내 계산을 진행하는 문제

코드의 구현은 어렵지 않으나... 해당 로직(순회중인 값이 +일땐 어떻게, ( 일땐 어떻게어떻게 등 등...)을 이해하는게 쉽지 않아 애를 먹었다...

```python
def calc(arr):
    stack = []
    for i in arr:
        if i in '0123456789':
            stack.append(int(i))
        else:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
    return stack.pop()

for tc in range(1, 11):
    N = int(input())
    arr = list(input())

    stack = []
    ans_list = [] # 우선순위가 앞인걸 후위표기식에선 앞에 적어줘야 함. 즉, 연산기호를 stack에 저장해둔 상태에서 넣어주는 중인 연산기호와 비교, 만약 우선순위가 더 높다면
    # 우선순위가 높은 것을 ans_list에 넣은 후 stack에 있는 연산기호를 pop -> append 해줌
    for i in arr:
        if i in '0123456789':
            ans_list.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans_list.append(stack.pop())
            stack.pop()
        elif i == '*':
            while stack and stack[-1] == '*':
                ans_list.append(stack.pop())
            stack.append(i)
        elif i == '+':
            while stack and stack[-1] != '(':
                ans_list.append(stack.pop())
            stack.append(i)
    while stack:
        ans_list.append(stack.pop())

    ans = calc(ans_list)
    print(f'#{tc} {ans}')
```

