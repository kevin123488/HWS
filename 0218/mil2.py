import sys

sys.stdin = open('mil_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    benefit = 0

    while len(arr) > 1:
        max_idx = arr.index(max(arr))
        benefit += max_idx * arr[max_idx] - sum(arr[:max_idx])
        arr = arr[max_idx + 1:]

    print(f'#{tc} {benefit}')