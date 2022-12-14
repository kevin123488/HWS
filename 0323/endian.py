import sys

print(sys.byteorder)
print()

a = 1234
# 정수 12를 8bit little endian으로 표시
n = int.to_bytes(a, byteorder='little', length=4)
print(n)
print()

# 정수 12를 8bit big endian으로 표시
n = int.to_bytes(a, byteorder='big', length=4)
print(n)
print()

print(int.from_bytes(n, byteorder='big'))
print(int.from_bytes(n, byteorder='little'))