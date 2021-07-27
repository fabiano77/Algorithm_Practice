s = input()
ans = []
for c in s:
    if ord(c)-3 >= ord('A'):
        ans.append(chr(ord(c)-3))
    else:
        ans.append(chr(ord(c)-2 + (ord('Z')-ord('A'))))
print(''.join(ans))