N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

def solve(N, stage, history):
    global M
    stage += 1
    for i in range(1, N+1):
        if len(history) > 0 and i <= history[-1]:
            continue
        else:
            cp_history = history.copy()
            cp_history.append(i)
            if stage == M:
                for item in cp_history:
                    print(item, end=' ')
                print()
            else:
                solve(N, stage, cp_history)


solve(N, 0, [])