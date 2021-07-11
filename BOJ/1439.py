s = input()
cnt_1 = 0
cnt_0 = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i-1] == '0':
            cnt_1 += 1
        else:
            cnt_0 += 1
if s[-1]=='0':
    cnt_1 += 1
else:
    cnt_0 += 1
print(min(cnt_1, cnt_0))