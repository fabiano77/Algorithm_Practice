n, b = input().split()
b = int(b)
ans = 0
digit = 0
n = list(map(str, n))
while n:
    a = n.pop()
    if a.isalpha():
        a = ord(a)-ord('A') + 10
    else:
        a = int(a)
    ans += a * (b ** digit)
    digit += 1
print(ans)