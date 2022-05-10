def soonyeul(n):
    # 정수 n을 받으면, 0부터 n-1까지의 숫자들로 구성된 (a, b) 형태의 숫자쌍을 뽑아내주는 함수
    # 다시 생각해 봤는데, 앞에 뽑은 2개를 제외한 것들중 2개를 뽑아 진행하는 방식으로 해야 할 것 같다
    # 다 뽑고 나면 그때까지의 값을 리스트에 저장해서 또다른 리스트에 넣어주는 형식으로 진행해야 할듯
    # ans_list = [[[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0, 3], [1, 2]]] 이런식으로 저장한 후
    # ans_list를 순회하며 sumfood 연산 후 그 값들을 정렬-2개씩 빼준 후 절댓값-그 값들 정렬- 제일 작은값 또다른 리스트에 담기-그 리스트 정렬 후 최솟값 뽑기
    # 이런 식으로 진행해야 한다 
    for k in range(n):
        num_list.append(k)
    i = 0    
    for i in range(n):
        for j in range(n):
            if i != j and i < j:
                ans_list.append([[i, j]])

    

ans_list = []
num_list = []
soonyeul(4)
print(ans_list)