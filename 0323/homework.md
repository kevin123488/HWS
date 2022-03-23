## 0323 HW

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 배열의 세로크기, M: 배열의 가로크기
    arr = [list(map(int, input())) for _ in range(N)]

    # 암호코드의 규칙
    # 8개의 숫자로 구성
    # 앞 7자리는 상품의 고유번호, 마지막 자리는 검증 코드
    # (홀수자리의 합 * 3) + 짝수자리의 합 + 검증코드 -> 10의 배수
    # 위의 조건을 만족한다 -> 제대로 된 암호코드
    # 배열 하나당 하나의 암호코드를 지니고 있음
    # 암호들은 끝자리가 1로 끝나는 공통점을 지니고 있음
    # 배열의 첫 줄을 끝부터 조회하다 1이 나오면? 7개씩 슬라이싱하여 정보를 얻어보자

    password = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    arr_password = []
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                x, y = j, i

    arr_password.append(arr[x][y-55:y+1])
    # arr_password에 암호에 대한 정보가 들어가게 되었다
    arr_k = arr_password[0]
    result = ''
    ans_list = []
    for i in range(0, len(arr_k), 7):
        for j in range(7):
            result += str(arr_k[i+j])
        if result in password:
            ans_list += [password[result]]
            result = ''

    # ans_list에 알맞은 값이 들어갔다. 이제 판별만 하면 됨
    if ((ans_list[0]+ans_list[2]+ans_list[4]+ans_list[6])*3 + ans_list[1]+ans_list[3]+ans_list[5] + ans_list[7])%10 == 0:
        print(f'#{tc} {sum(ans_list)}')
    else:
        print(f'#{tc} 0')
```

