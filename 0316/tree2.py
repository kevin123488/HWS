# 완전이진트리 에서의 순회

# def pre(v):
#     global last
#     if v <= last: # 마지막 정점번호 이내
#         print(v) # visit(v)
#         pre(v*2) # 왼쪽 자식 방문
#         pre(v*2+1) # 오른쪽 자식 방문

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 99]
for i in arr:
    if type