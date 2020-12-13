import sys

count = 0

def promising(row, col):
    global columns
    for ro in range(0, row):
        #if columns[ro] == col:
        #    return False
        if abs(ro - row) == abs(columns[ro]- col):
            return False
    return True

def queen_solve(row):
    global columns
    global max
    global count
    for co in range(0, max):
        if co not in columns[:row]:
            if promising(row, co):
                if row == max - 1:
                    count = count+1
                    return
                columns[row] = co
                queen_solve(row+1)
    return

N = int(input())
columns = [ 0 for _ in range(N)]

max = N
queen_solve(0)
print(count)
