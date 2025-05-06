A = int(input())

for i in range(1, A + 1):
    cond1 = (i % 2 == 0 and i % 4 != 0)
    cond2 = ((i // 8) % 2 == 0)
    cond3 = (i % 7 < 4)

    if not (cond1 and cond2 and cond3):
        print(i, end=' ')
