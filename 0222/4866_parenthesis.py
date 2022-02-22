import sys
sys.stdin = open('4866_input.txt')

T = int(input())
for tc in range(1, T+1):
    str_to_cheak = list(input())

    # stack을 만들자
    stack = []
    find = []
    parenthesis = ['(', ')', '{', '}']

    for i in range(len(str_to_cheak)):
        if str_to_cheak[i] in parenthesis:
            find.append(str_to_cheak[i])

    # find에 괄호의 정보가 담겨있음
    for k in range(len(find)):
        if stack == []: # stack이 비어있을땐
            stack.append(find[k]) # 뭐라도 넣어줘라
        elif stack[-1] == '(': # stack이 ( 일때
            if find[k] == ')': # 닫을 수 있는 친구가 나오면
                stack.pop() # stack의 (를 지워줘라
            else: # 닫을 수 있는 친구 외의 경우엔
                stack.append(find[k]) # 못닫았으니 그냥 추가해라
        elif stack[-1] == '{': # stack이 { 일때
            if find[k] == '}': # 닫을 수 있는 친구가 나오면
                stack.pop() # stack의 {를 지워줘라
            else: # 닫을 수 있는 친구 외엔
                stack.append(find[k]) # 못닫았으니 그냥 추가해라
        else: # stack이 채워져있고, [-1]의 값이 여는 괄호가 아닐 때
            stack.append(find[k]) # 못닫으니까 값을 추가해줘라

    if len(stack): # stack의 길이가 0이 아니면
        print(f'#{tc} 0') # 안닫히고 남은 괄호가 있는거니, 0 출력
    else: # stack의 길이가 0이면
        print(f'#{tc} 1') # 모두 다 닫힌거니, 1 출력