s = list(map(str, input()))
ans = []
for c in s:
    if c not in 'CAMBRIDGE':
        ans.append(c)
print(''.join(ans))
