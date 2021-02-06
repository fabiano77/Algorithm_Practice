def trans_36_to_int(num_36):
    if num_36.isnumeric():
        return ord(num_36)-ord('0')
    return (ord(num_36)-ord('A')) + 10

def trans_int_to_36(num_int):
    if num_int <= 9:
        return chr(num_int + ord('0'))
    return chr(num_int - 10 + ord('A'))

cnt = [0] * 36
for _ in range(int(input())):
    numbers_36 = input()
    for i, num in enumerate(numbers_36[::-1]):
        cnt[trans_36_to_int(num)] += 36**i
# print(cnt)

profit = [0] * 36
for i in range(36):
    profit[i] = cnt[i] * (35 - i)
profit = list(zip(range(36), profit))
profit.sort(key = lambda x : x[1], reverse=True)

result_int = 0

k = int(input())
for i in range(k):
    num = profit[i][0]
    # print(f'{i}번째로 이득이 큰 {num}을 선택')
    result_int += cnt[num] * 35
    cnt[num] = 0

for i in range(36):
    result_int += cnt[i] * i

# print(result_int)
result_36 = ''
if result_int == 0:
    result_36 += '0'
else:
    while result_int:
        num_int = result_int % 36
        result_int //= 36
        result_36 += trans_int_to_36(num_int)

print(result_36[::-1])

