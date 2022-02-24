import sys
sys.stdin = open('forth_input.txt')

# 후위표기법으로 작성된 입력값을 받는다. 올바른 식일 경우 값을 내고, 올바르지 않을 경우 error를 출력하자
T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())

    stack = []
    for i in range(len(arr)):
        if arr[i] in '+-*/.':
            if arr[i] == '+':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '*':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '-':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '/':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b//a)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '.':
                if len(stack) == 1:
                    print(f'#{tc} {stack[-1]}')
                    break
                else:
                    print(f'#{tc} error')
                    break
        else:
            stack.append(int(arr[i]))
