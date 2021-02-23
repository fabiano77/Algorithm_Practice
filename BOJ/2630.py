n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

result = {0: 0, 1: 0}

def solve(row, col, n):
    first = data[row][col]
    consensus = True
    for i in range(row, row+n):
        if not consensus: break
        for j in range(col, col+n):
            if data[i][j] != first:
                consensus = False
                break
    
    if consensus:
        result[first] += 1
    else:
        n //= 2
        solve(row, col, n)
        solve(row, col+n, n)
        solve(row+n, col, n)
        solve(row+n, col+n, n)

solve(0, 0, n)

print(result[0])
print(result[1])