import sys

sys.stdin = open('input.txt')

for tc in range(1, 11): # 10개의 test case 주어짐
    N = int(input()) # N은 가장 먼저 입력받는 값으로, 뒤에 나올 값들의 개수를 의미
    data = list(map(int, input().split())) # 여러개의 값을 받아 정수로 변환해준 후 list에 담기
    ans = 0

    for i in range(2, N-2): # 입력받는 값중 앞 2개, 끝 2개는 필요 ㄴ.
        # 주변 4개의 건물중 가장 높다면? 반드시 조망권 O.
        # 조사중인 건물의 높이와 주변 4개중 가장 높은 건물의 높이를 빼주면? -> 해당 건물의 조망권 O인 세대의 수가 나옴.
        around = [data[i-2], data[i-1], data[i+1], data[i+2]]
        if data[i] > data[i - 1] and data[i] > data[i - 2] and data[i] > data[i + 1] and data[i] > data[i + 2]:
            ans += data[i] - max(around)

    print(f'#{tc} {ans}')