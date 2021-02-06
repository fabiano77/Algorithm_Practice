n = int(input())
lst = list(map(int, input().split()))

dp = [lst[0]]
'''
1 2 1 3 2 5
1 2 2 3 3 4
'''
for item in lst:
    if item > dp[-1]:
        dp.append(item)
    else:
        for i, x in enumerate(dp):
            if item == x:
                break
            if item < x:
                dp[i] = item
                break
print(len(dp))