s = input()
cnt = 0
items = ['a', 'e', 'i', 'o', 'u']

for item in items:
    cnt += s.count(item)

print(cnt)