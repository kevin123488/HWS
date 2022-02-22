import sys
sys.stdin = open('4873_input.txt')

# stack을 사용해보자
T = int(input())
for tc in range(1, T+1):
    str_to_cheak = list(input())

    # 빈 스택을 만들자
    stack = []
    # 받은 리스트를 조회하며 앞의것과 중복되지 않으면 stack에 해당 원소를 넣고, 중복되면 stack의 해당 원소를 빼자
    for i in range(len(str_to_cheak)):
        if stack == []:
            stack.append(str_to_cheak[i])
        elif str_to_cheak[i] == stack[-1]:
            stack.pop()
        elif str_to_cheak[i] != stack[-1]:
            stack.append(str_to_cheak[i])

    print(f'#{tc} {len(stack)}')