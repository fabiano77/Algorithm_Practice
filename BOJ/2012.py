li = sorted([int(input())  for _ in range(int(input()))])
a = 0
for i in range(len(li)):
    a += abs(li[i] - (i+1))
print(a)