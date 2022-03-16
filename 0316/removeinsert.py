'''
최대 100개의 정수가 키로 입력됨
최대 힙
'''

def enq(n): # 삽입하기
    global last
    last += 1
    tree[last] = n # 완전이진트리 유지
    # 최대 힙 관리
    c = last # 새로 추가된 정점을 자식으로
    p = c//2 # 완전이진트리 에서의 부모 정점 번호
    while p >= 1 and tree[p] < tree[c]: # 부모가 있고, 자식의 키값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq(): # 삭제하기
    global last
    tmp = tree[1] # 루트의 key값 tmp에 저장
    tree[1] = tree[last] # 마지막 정점의 키를 루트에 복사
    last -= 1 # 마지막 정점 삭제
    # 부모 -> 자식 규칙 유지
    p = 1
    c = p * 2 # 왼쪽 자식노드 번호
    while c <= last: # 왼쪽자식이 있으면
        if c+1 <= last and tree[c] < tree[c+1]: # 오른쪽 자식이 더 크면
            c += 1 # 오른쪽 자식 선택
        if tree[p] < tree[c]: # 만약 자식이 더 크면
            tree[p], tree[c] = tree[c], tree[p] # 교환하기
            p = c
            c = p*2
        else:
            break
    return tmp

# 포화이진트리의 정점번호 1~100
tree = [0]*101 # 0번 인덱스는 빼두고, 1번부터 진행되므로
last = 0 # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
enq(9)
while last > 0:
    print(deq(), tree[1])