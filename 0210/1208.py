import sys
sys.stdin = open('1208_input.txt')

# 버블정렬
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

for tc in range(1, 11):
    dump = int(input())
    width_list = list(map(int, input().split()))

    for k in range(dump):
        list_sorted = bubble_sort(width_list)
        list_sorted[-1] -= 1
        list_sorted[0] += 1
        if bubble_sort(list_sorted)[-1] - bubble_sort(list_sorted)[0] == 0 or bubble_sort(list_sorted)[-1] - bubble_sort(list_sorted)[0] == 1:
            print(f'#{tc} {list_sorted[-1] - list_sorted[0]}')
        else:
            pass

    print(f'#{tc} {list_sorted[-1] - list_sorted[0]}')
