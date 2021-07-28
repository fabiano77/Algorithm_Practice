n, k = map(int, input().split())
li = list(map(int, input().split()))
start = 0
end = k
t = sum(li[start:end])
ans = t
while end < n:
    t -= li[start]
    t += li[end]
    start += 1
    end += 1
    ans = max(ans, t)
print(ans)