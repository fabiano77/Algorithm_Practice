n = int(input())
li = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
for i in range(n):
    if i%3 == 2:
        continue
    cnt += li[i]
print(cnt)
