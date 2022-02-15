import sys
sys.stdin = open('4839_이진탐색_input.txt')

T = int(input())

# 이진탐색을 위해 함수를 만들자
def binary_count(whole, find):
    start = 0
    count = 0
    while start <= whole:
        middle = (start + whole)//2
        if middle == find:
            count += 1
            return count
        elif middle < find:
            count += 1
            start = middle
        elif middle > find:
            count += 1
            whole = middle

for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    # p는 전체 쪽 수, a는 a가 찾아야하는 쪽, b는 b가 찾아야하는 쪽

    count_a = binary_count(p, a)
    count_b = binary_count(p, b)

    if count_a > count_b:
        print(f'#{tc} B')
    elif count_a < count_b:
        print(f'#{tc} A')
    elif count_a == count_b:
        print(f'#{tc} 0')