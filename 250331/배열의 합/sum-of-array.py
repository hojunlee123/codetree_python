matrix = [list(map(int, input().split())) for _ in range(4)]

for row in matrix:
    print(sum(row))
