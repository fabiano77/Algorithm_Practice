s = input()
ans = []
for c in s:
    if c.isalpha():
        if c.isupper() and ord(c)+13 > ord('Z'):
            ans.append(chr(ord(c)+12 - (ord('Z') - ord('A'))))
        elif c.islower() and ord(c)+13 > ord('z'):
            ans.append(chr(ord(c)+12 - (ord('z') - ord('a'))))
        else:
            ans.append(chr(ord(c)+13))
    else:
        ans.append(c)
        
print(''.join(ans))
    