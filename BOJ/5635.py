li = []
for _ in range(int(input())):
    name, dd, mm, yyyy = input().split()
    li.append((name, int(dd), int(mm), int(yyyy)))
li.sort(key=lambda x:(x[3], x[2], x[1]))
print(li[-1][0])
print(li[0][0])