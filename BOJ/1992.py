n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

ans = ''

def solve(n, r, c):
    global ans

    first = graph[r][c]
    all_same = True
    for i in range(r, r+n):
        for j in range(c, c+n):
            if first != graph[i][j]:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        ans += str(first)
    elif n >= 1:
        # if n != 1: 
        ans += '('
        n //= 2
        solve(n, r, c)
        solve(n, r, c+n)
        solve(n, r+n, c)
        solve(n, r+n, c+n)
        # if n != 1:
        ans += ')'
    
    return

solve(n, 0, 0)    

print(ans)