import sys
sys.stdin = open('samsungbus_input.txt')

# 1부터 5000까지의 번호가 붙어있는 버스 정류장
# N개의 버스 노선. i번째 버스 노선은 번호가 Ai <= <= Bi인 모든 버스정류을 다님
# p개의 버스 정류장에 대해, 각 버스 정류장에 몇 개의 버스 노선이 지나는지 출력하라

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 노선의 개수
    AiBilist = [list(map(int, input().split())) for _ in range(N)] # Ai와 Bi값을 리스트에 담아줌
                                                                   # [[A1, B1], ... , [Ai, Bi]] 이런 식으로 받아질듯
    # AiBilist를 하나씩 순회하며 Ai<=<=Bi인 리스트에 해당하는 값을 또다른 리스트에 담아보자
    p = int(input()) # p개의 정류장
    p_list = [int(input()) for __ in range(p)] # p개의 정류장 번호를 리스트에 담자
    ans_list = [0]*p # 여기에 Ai<=<=Bi에 해당하는 부분을 +=1 해줄것이다

    for i in AiBilist:
        for jungryu in range(len(p_list)):
            if i[0] <= p_list[jungryu] <= i[1]:
                ans_list[jungryu] += 1


    print(f'#{tc}', *ans_list)