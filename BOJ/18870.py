n = int(input())
data = list(map(int, input().split()))
ordered_data = list(map(list, zip(range(0, len(data)), data)))
ordered_data.sort(key = lambda x:x[1])
cnt = -1
for i in range(len(data)):
    if not(i > 0 and ordered_data[i][1] == ordered_data[i-1][1]):
        cnt += 1
    ordered_data[i].append(cnt)
ordered_data.sort(key = lambda x:x[0])
for item in ordered_data:
    print(item[2], end=' ')
