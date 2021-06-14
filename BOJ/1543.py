a = input()
b = input()

index = 0
ans = 0
while True:
    index = a.find(b, index)
    if index == -1:
        break
    ans += 1
    index += len(b)
print(ans)