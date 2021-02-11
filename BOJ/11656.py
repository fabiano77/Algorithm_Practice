s = input()
lst = []
for i in range(len(s)):
    lst.append(s[i:])
lst.sort()
for a in lst:
    print(a)