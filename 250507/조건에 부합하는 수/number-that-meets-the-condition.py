A = int(input())

for i in range(1, A + 1):
    cond1 = not (i % 2 == 0 and i % 4 != 0)
    cond2 = not ((i // 8) % 2 == 0)
    cond3 = not (i % 7 < 4)

    if cond1 and cond2 and cond3:
        print(i, end=' ')
