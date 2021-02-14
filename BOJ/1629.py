# a를 b번 곱한 수를 c로 나눈 나머지

a, b, c = map(int, input().split())
dict_arr = dict()

def pow(a, b):
    global c
    global dict_arr
    str_b = str(b)

    if str_b in dict_arr:
        return dict_arr[str_b]

    if b <= 1:
        dict_arr[str_b] = (a ** b) % c
    elif b % 2 == 0:
        dict_arr[str_b] = (pow(a, b//2) * pow(a, b//2)) % c
    else:
        dict_arr[str_b] = (pow(a, b//2) * pow(a, (b//2)+1)) % c

    return dict_arr[str_b]

print(pow(a, b))