n, m = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
ans = []

index_a = 0
index_b = 0


while index_a < n or index_b < m:
    if index_a == n:
        ans.append(li_b[index_b])
        index_b += 1
    elif index_b == m:
        ans.append(li_a[index_a])
        index_a += 1
    else:
        if li_a[index_a] < li_b[index_b]:
            ans.append(li_a[index_a])
            index_a += 1
        else:
            ans.append(li_b[index_b])
            index_b += 1

for i in ans:
    print(i, end =' ')