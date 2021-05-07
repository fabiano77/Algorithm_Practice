a = input()
b = input()
start_time = int(a[0:2]) * 3600 + int(a[3:5]) * 60 + int(a[6:])
target_time = int(b[0:2]) * 3600 + int(b[3:5]) * 60 + int(b[6:])

solution_time = target_time - start_time
if solution_time < 0:
    solution_time += 24 * 3600

hour = solution_time // 3600
minute = (solution_time // 60) - hour * 60
second = solution_time % 60
answer = f'{hour:02d}:{minute:02d}:{second:02d}'
print(answer)