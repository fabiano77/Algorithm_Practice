data = []
for i in range(8):
    data.append((int(input()), i+1))
data.sort(key = lambda x: x[0], reverse=True)
print(sum(map(lambda x: x[0], data[:5])))
data = sorted(data[:5], key = lambda x:x[1])
for i in data:
    print(i[1], end=' ')