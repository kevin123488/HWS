import sys
sys.stdin = open('1208_input.txt')

# test case 10개
for tc in range(1, 11):
    # dump 횟수 입력받기
    dump = int(input())
    box_height = list(map(int, input().split()))

    # box_height의 최댓값과 최솟값을 인덱스로 뽑아온 후, 해당 값을 각각 -=1, +=1 해준다
    a = max(box_height)
    b = min(box_height)
    c = box_height.index(a)
    d = box_height.index(b)

    print(c, d)