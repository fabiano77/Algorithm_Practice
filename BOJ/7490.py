def solve(depth, string, N):
  string = string + str(depth)
  if depth == N:
    if eval(string.replace(' ', '')) == 0 :
      print(string)
    return
  for operator in " +-":
    new_string = string + operator
    solve(depth+1, new_string, N)


T = int(input())
for _ in range(T):
  N = int(input())
  solve(1, "", N)
  print()