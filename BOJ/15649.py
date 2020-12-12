import copy

N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def tracking(history, i, depth, max_depth):
    if depth != 0:
        history.append(i)
    if depth == max_depth: 
        for item in history: 
            print(item, end=' ')
        print()
        return
    for j in range(1, N+1):
        if j not in history:
            history_cp = copy.copy(history)
            tracking(history_cp, j, depth+1, max_depth)

tracking([], 0, 0, M)