n = int(input())
lst = list(map(int, input().split()))

def longest(lst):
    dp = []
    for item in lst:
        if not dp or item > dp[-1]:
            dp.append(item)
        else:
            for i, x in enumerate(dp):
                if item == x:
                    break
                if item < x:
                    dp[i] = item
                    break
    return dp

def shortest(lst):
    dp2 = []
    for item in lst:
        if not dp2 or item < dp2[-1]:
            dp2.append(item)
        else:
            for i, x in enumerate(dp2):
                if item == x:
                    break
                if item > x:
                    dp2[i] = item
                    break
    return dp2

sol = 0
for i in range(len(lst)):
    dp = longest(lst[:i]) 
    dp2 = shortest(lst[i:])
    if dp and dp2 and dp[-1] == dp2[0]:
        dp.pop()
    temp = dp + dp2
    if sol < len(temp):
        sol = len(temp)

print(sol)