s = input()
ans = ''
for ch in s:
    if ch.isupper():
        ans += ch.lower()
    else:
        ans += ch.upper()
print(ans)