n = int(input())
li = list(map(int, input().split()))
target = int(input())
ans = 0

li.sort()
a, b = 0, len(li)-1

while a < b:
    if li[a]+li[b] == target:
        ans += 1
        a += 1
        b -= 1
    elif li[a]+li[b] > target:
        b -= 1
    elif li[a]+li[b] < target:
        a += 1
print(ans)