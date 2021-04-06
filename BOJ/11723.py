import sys
input = lambda: sys.stdin.readline().rstrip()
myset = [False]*21
for _ in range(int(input())):
    cmd = list(input().split())
    if len(cmd) >= 2: 
        num = int(cmd[1])
    if cmd[0] == 'add':
        myset[num] = True
    elif cmd[0] == 'remove':
        if myset[num]:
            myset[num] = False
    elif cmd[0] == 'check':
        print(int(myset[num]))
    elif cmd[0] == 'toggle':
        myset[num] = not myset[num]
    elif cmd[0] == 'all':
        myset = [True]*21
    elif cmd[0] == 'empty':
        myset = [False]*21