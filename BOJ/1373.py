ans = []
oct = input()
oct2binary = ['000', '001', '010', '011', '100', '101', '110', '111']
first = ['0', '1', '10', '11', '100', '101', '110', '111']
ans += first[int(oct[0])]
for d in oct[1:]:
    ans.append(oct2binary[int(d)])

print(''.join(ans))