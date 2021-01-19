import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

print(round(sum(array)/len(array)))
print(array[len(array)//2])

prev = ''
cnt = 0
cnt_max = 0
mode = []

for i in range(len(array)):
    if array[i] != prev or cnt == 0:
        cnt = 1
        prev = array[i]
    else:
        cnt += 1

    if cnt > cnt_max:
        mode = []
        cnt_max = cnt
        mode.append(array[i])
    elif cnt == cnt_max:
        mode.append(array[i])

mode.sort()
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

print(array[-1]-array[0])