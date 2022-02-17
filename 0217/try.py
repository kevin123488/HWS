# 1. 조원의 수를 M, 리스트의 크기 N (M < N < M**3)이 주어졌을 때,
# - 각 조원은 0부터 M-1까지의 고유 번호를 가진다.
# 2. 크기 N인 리스트에 그날 발표할 문제 번호들을 무작위 인덱스에 삽입한다.
# [0, 0, 0, 0, '글자수', 0, 0, 0, 0, '문자열 비교', 0, 0, 0, 0, 0, 'GNS', 0, 0, 0, 0, 0, 0, 0, 0]
#
# 3. 각 문제의 위치를 바이너리 서치로 탐색한다.
# - 각 문항이 몇번째 인덱스에 들어있는지
# - 각 문항을 찾는데 몇번의 탐색이 필요했는지
# 4. 위의 각 두 값을 더한다음 조원수 M으로 나눈 나머지가 조원의 고유 번호와 일치하는 사람이 발표한다.
import sys
import random

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

sys.stdin = open('try.txt')

M, N = map(int, input().split()) # M은 멤버 수, N은 리스트의 길이
list_of_team = [0]*N
# 문제의 종류는 총 2개(회문, 회문2)
ran_num_idx = random.sample(range(N), 2)

for1_idx = ran_num_idx[0]
for2_idx = ran_num_idx[1]
list_of_team[for1_idx] = '회문'
list_of_team[for2_idx] = '회문2'

# 계산
ans_1 = ((binary_count(N, for1_idx) + for1_idx) % M)
ans_2 = ((binary_count(N, for2_idx) + for2_idx) % M)
print(f'{list_of_team[for1_idx]} 문제는 {ans_1+1}, {list_of_team[for2_idx]} 문제는 {ans_2+1}')