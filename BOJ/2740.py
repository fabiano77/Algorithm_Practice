def mul(mat1, mat2):
    ret = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            val = 0
            for k in range(len(mat1[0])):
                val = ( val + mat1[i][k] * mat2[k][j] )
            row.append(val)
        ret.append(row)
    return ret

mat1 = []
mat2 = []

n, b = map(int, input().split())
for _ in range(n):
    mat1.append(list(map(int, input().split())))
m, k = map(int, input().split())
for _ in range(m):
    mat2.append(list(map(int, input().split())))

sol = mul(mat1, mat2)
for row in sol:
    for item in row:
        print(item, end= ' ')
    print()

    