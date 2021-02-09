
k = int(input())

data = input()
lst = []
for i in range(len(data)//k):
    if i % 2 == 0:
        lst.append(data[i*k:i*k+k])
    else:
        lst.append("".join(reversed(data[i*k:i*k+k])))

for i in range(k):
    for j in range(len(data)//k):
        print(lst[j][i], end= "")
print()