
S = input()
T = input()
def solve(str):
  if not str: return
  if str == S:
    print(1)
    exit()
  if str[-1] == 'A' : solve(str[:len(str)-1])
  if str[0]  == 'B' : solve(str[:0:-1])
solve(T)
print(0)

