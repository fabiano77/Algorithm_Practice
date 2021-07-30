s = input()
flag = True
start_index = 0
for a in ['U', 'C', 'P', 'C']:
    if s.find(a, start_index) != -1:
        start_index = s.find(a, start_index) + 1
    else:
        flag = False
        break
if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")