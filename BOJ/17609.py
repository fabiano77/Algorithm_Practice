def solve(front, back, similar):
    global s
    while front < back:
        if s[front] == s[back]:
            front += 1
            back -= 1
        else:
            similar += 1
            if similar == 2:
                break
            else:
                result = 2
                if s[front+1] == s[back]:
                    result = min(result, solve(front+1, back, 1))
                if s[front] == s[back-1]:
                    result = min(result, solve(front, back-1, 1))
                return result
    return similar

for _ in range(int(input())):
    s = input()
    front, back = 0, len(s)-1
    print(solve(front, back, 0))

