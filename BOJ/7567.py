data = input()

prev = 0
ans = 0

for i in data:
    if i == prev:
        ans += 5
    else:
        ans += 10
    prev = i

print(ans)