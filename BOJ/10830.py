n, b = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
eye = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    eye.append(row)


dp = dict()

def pow(mat, b):
    global dp
    str_b = str(b)
    if str_b in dp:
        return dp[str_b]
    if b == 0:
        return

    if b == 1:
        dp[str_b] = mat
    elif b % 2 == 0:
        dp[str_b] = mul(pow(mat, b//2), pow(mat, b//2))
    else:
        dp[str_b] = mul(pow(mat, b//2), pow(mat, (b//2) + 1))

    return dp[str_b]


def mul(mat1, mat2):
    ret = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            val = 0
            for k in range(len(mat1[0])):
                val = ( val + mat1[i][k] * mat2[k][j] )%1000
            row.append(val)
        ret.append(row)
    return ret

mat = mul(mat, eye)
result = pow(mat, b)

for i in range(n):
    for j in range(n):
        print(result[i][j], end = ' ')
    print()