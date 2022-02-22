import sys
sys.stdin = open('4869_input.txt')

def answer(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return answer(N-20) + 2**((N-10)/10)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 가로의 길이 N은 10의 배수
    # 세로 20, 가로 10인 직사각형과 세로 20, 가로 20인 직사각형을 이용하여
    # 세로 20, 가로 N인 직사각형을 가득 채우려 할 때, 가능한 경우의 수를 모두 구하여라
    # 규칙 -> N이 10일때 ans = 1
    # N이 20일때 ans = 3
    # 그 외의 N에 대해 ans = (20낮은 N에 대한 값) + 2**((N-10)/10)

    print(f'#{tc} {round(answer(N))}')