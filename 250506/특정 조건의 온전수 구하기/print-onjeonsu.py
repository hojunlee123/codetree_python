N = int(input())

for i in range(1, N + 1):
    if i % 2 != 0 and i % 10 != 5 and (i % 3 != 0 or i % 9 == 0):
        print(i, end=' ')
