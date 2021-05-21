n = int(input())
for i in sorted(list(set(map(int, input().split())))):
    print(i, end=' ')