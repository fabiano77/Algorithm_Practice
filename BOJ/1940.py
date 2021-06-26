n = int(input())
m = int(input())
li = sorted(list(map(int, input().split())))
start, end = 0, len(li)-1
cnt = 0
while start < end:
    num = li[start]+li[end]
    if num == m:
        cnt += 1
        start += 1
        end -= 1
    elif num > m:
        end -= 1
    elif num < m:
        start += 1
print(cnt)