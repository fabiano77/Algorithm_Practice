import sys

# data = sys.stdin.readline().rstrip()


def bin_search(array, first, last, target):
    if first > last:
        return None
    mid = (first + last)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return bin_search(array, mid+1, last, target)
    else:
        return bin_search(array, first, mid-1, target)


N, M = map(int, input().split())

a_list = []
b_list = []

for _ in range(N):
    a_list.append(sys.stdin.readline().rstrip())
    # a_list.append(input())
a_list.sort()


for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    # temp = input() 입력 부분을 바꿨더니 4192ms->376ms 차이남
    if bin_search(a_list, 0, N-1, temp) is not None:
        b_list.append(temp)

b_list.sort()
print(len(b_list))
for item in b_list:
    print(item)