k = int(input())
for i in range(k):
    li = list(map(int, input().split()))
    n = li[0]
    li = sorted(li[1:])
    print(f'Class {i+1}')
    print(f'Max {max(li)}, Min {min(li)}, Largest gap {max(list(abs(li[i] - li[i-1]) for i in range(1, len(li))))}')
