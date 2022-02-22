import sys
sys.stdin = open('4869_input.txt')

# memo 사용

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    memo = [0, 1, 3] # N이 10일때와 20일때의 값을 넣어줘야됨

    for i in range(1, 31):
        if i > 2:
            memo.append(memo[i-2]+2**(i-1))

    print(f'#{tc} {memo[N]}')