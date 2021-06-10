# 모든 순열

n = int(input())

def print_list(li):
    for item in li:
        print(item, end=' ')
    print()

def solve(n, mem):
    for i in range(1, n+1):
        if i in mem:
            continue
        mem.append(i)
        if len(mem) == n:
            print_list(mem)
            return
        else:
            solve(n, list(mem))
        mem.pop()

solve(n, [])