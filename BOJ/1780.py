result = {-1: 0, 0: 0, 1: 0}

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

def solve(row, col, n):
    global result

    first = data[row][col]
    consensus = True
    for i in range(row, row + n):
        if not consensus: break
        for j in range(col, col + n):
            if data[i][j] != first:
                consensus = False
                break
    if consensus:
        result[first] += 1

    else:
        n //= 3
        for i in range(3):
            for j in range(3):
                solve(row + i*n, col + j*n, n)

solve(0, 0, n)

for key in result:
    print(result[key])