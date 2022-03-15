import sys
sys.stdin = open('hoijeun.txt')

T = int(input()) # 테스트 케이스의 개수
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 숫자의 개수, M: 맨 앞의 숫자를 뒤로 보내는 작업의 횟수
    num_list = list(map(int, input().split())) # num_list: N개의 숫자로 이뤄진 수열

    # 한번 뒤로 넘기면? 두번째 숫자가 가장 앞. 두번? 세번째 숫자. N번 뒤로 넘기면? 첫번째 숫자가 가장 앞. 즉 %를 이용하면 간단히 풀린다는 소리.
    # M을 N으로 나눈 나머지에 집중. 나머지의 인덱스를 가지는 값을 출력하면 됨.
    ans_index = M % N
    ans = num_list[ans_index]

    print(f'#{tc} {ans}')