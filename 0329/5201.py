# 컨테이너 운반
import sys
sys.stdin = open('input_5201.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 컨테이너의 수, M: 트럭의 수
    w = list(map(int, input().split())) # 컨테이너의 무게 정보
    t = list(map(int, input().split())) # 트럭의 적재용량 정보

    # 한 대의 트럭으로 1개의 컨테이너만 운송 가능, 해당 트럭의 적재용량을 초과한 컨테이너는 그 트럭으로 운반 불가
    # 운송한 화물의 무게가 최대가 되도록 운반했을 때, 그 때의 총 운반량을 출력하여라
    # 아무것도 운반하지 못하는 경우 또한 가능
    ans = 0
    for i in range(len(t)): # 트럭을 기준으로 해보자
        que = []
        for j in range(len(w)): # 각 트럭당 해당 트럭의 적재용량과 가장 비슷한 값을 넣어 더해주면 될 것 같음
            if t[i] >= w[j]: # 트럭이 싣고 갈 수 있는 양이면
                que.append(w[j]) # que에 해당 무게를 담아주자
        if que:
            que.sort() # que 오름차순으로 정렬해주고
            ans += que[-1] # 제일 큰 값을 더해준 후
            idx = w.index(que[-1]) # 그 값이 들어있던 자리를
            w[idx] = 0 # 0으로 바꿔주자

    print(f'#{tc} {ans}')