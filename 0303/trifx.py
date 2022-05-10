import math

def atan(x):
    y = math.atan(x)
    return y

now_where = [0, 0]
target_where = [3, 6]
# target_where의 위치에 따라(몇 사분면인가) 다른 공식을 적용해야 할 듯
# 1사분면( target_where의 x, y좌표 모두 now_where의 x, y좌표보다 큰 값)일 때 -> blabla
# 2사분면
# 3사분면
# 4사분면

angle = atan((target_where[1]-now_where[1])/(target_where[0]-now_where[0]))

print(angle)