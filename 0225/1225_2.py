import sys
sys.stdin = open('1225_input.txt')

# 8개의 숫자를 입력받음
# 첫 숫자는 1 감소시킨 후 제일 뒤로 보냄
# 두번째는 2 감소시킨 후 제일 뒤로 보냄
# 그렇게 감소수치를 1씩 증가시키다 다섯번째 숫자를 5 감소시켜 가장 뒤로 보낸 후 다시 감소수치 1로 초기화

def cycle(arr):
    i = 1
    while i < 6:
        a = arr.pop(0) # 가장 앞의 값을 뽑아낸 후 a에 담기
        if a - i <= 0: # 만약 가장 앞의 값에서 i를 뺀 값이 음수라면?
            arr.append(0) # arr에 -1이라는 값을 append 해줌
            break # 그리고 종료조건에 다다랐으므로 break
        else: # 그 외의 경우
            arr.append(a-i) # 계산한 결과를 append 해줌
        i += 1
    return

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 받은 arr를 cycle 돌린 후 결과를 출력하자
    while True:
        cycle(arr) # cycle 함수를 계속 돌려보자
        # 종료조건을 설정해야 한다
        if 0 in arr:
            break # cycle을 돌고 난 후 arr에 0이 포함되어있다면 break하고 결과 내기

    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()