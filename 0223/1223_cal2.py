import sys
sys.stdin = open('1223_cal2_input.txt')

# 계산식을 후위표기식으로 바꾸어라
# 계산식 구성 연산자는 +와 *
# 3+4+5*6+7 이라는 식의 경우 34+56*+7+ 로 바뀐다

# 우선순위 결정
def whichisfast(a):
    if a in '1234567890':
        return 1
    elif a == '+':
        return 2
    else:
        return 3

# 10개의 tc
for tc in range(1, 11):
    N = int(input())
    arr = list(input())

    stack = [] # 빈 스택을 만들어줌
    ans_list = [] # 답안을 넣을 리스트를 만들어줌

    for i in range(N):
        if ans_list == []:
            ans_list += [arr[i]]
        elif arr[i] in '1234567890':
            ans_list += [arr[i]]
        else:
            if stack == []:
                stack.append(arr[i])
            elif whichisfast(arr[i]) >= whichisfast(stack[-1]):
                stack.append(arr[i])
            else:
                ans_list.append(stack.pop())
    print(f'#{tc} {ans_list}')

    stack = []
    for k in range(len(ans_list)):
        if ans_list[k] in '1234567890':
            stack += [int(ans_list[k])]
        elif ans_list[k] == '+':
            a = stack.pop()
            b = stack.pop()
            stack += [a+b]
        elif ans_list[k] == '*':
            a = stack.pop()
            b = stack.pop()
            stack += [a*b]

    print(f'#{tc} {stack[-1]}')