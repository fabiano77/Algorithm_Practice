s = input()

t = True
for i in range(len(s)//2+1):
    if s[i] != s[-(i+1)]:
        t = False
        break
print(int(t))    